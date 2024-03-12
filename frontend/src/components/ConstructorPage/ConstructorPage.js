import React, { useState, useEffect, useRef } from 'react';
import axios from 'axios';
import './ConstructorPage.css';

const ConstructorPage = () => {
  const [interviewName, setInterviewName] = useState('');
  const [tasks, setTasks] = useState([]);
  const [selectedTasks, setSelectedTasks] = useState([]);
  const [error, setError] = useState('');
  const taskListRef = useRef(null);

  useEffect(() => {
    axios.post('http://0.0.0.0:8000/task/get_all')
      .then(response => {
        const responseData = response.data;
        if (responseData && responseData.tasks && Array.isArray(responseData.tasks)) {
          setTasks(responseData.tasks);
        } else {
          console.error('Invalid data format for tasks:', responseData);
        }
      })
      .catch(error => {
        console.error('Error fetching tasks:', error);
      });
  }, []);

  useEffect(() => {
    const taskList = taskListRef.current;
    if (taskList) {
      const taskElements = Array.from(taskList.children);
      const totalHeight = taskElements.reduce((acc, task) => acc + task.offsetHeight, 0);
      if (totalHeight > taskList.offsetHeight) {
        const fontSize = parseFloat(window.getComputedStyle(taskElements[0]).fontSize);
        const newFontSize = fontSize - 2;
        taskElements.forEach(task => {
          task.style.fontSize = `${newFontSize}px`;
        });
      }
    }
  }, [tasks]);

  const getRandomColor = () => {
    const letters = '0123456789ABCDEF';
    let color = '#';
    for (let i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
  };

  const handleDragStart = (e, task) => {
    e.dataTransfer.setData('task', JSON.stringify(task));
  };

  const handleDrop = (e) => {
    const task = JSON.parse(e.dataTransfer.getData('task'));
    if (!selectedTasks.some(selectedTask => selectedTask.name === task.name)) {
      setSelectedTasks([...selectedTasks, { ...task, color: getRandomColor() }]);
    }
  };

  const handleInputChange = (e) => {
    setInterviewName(e.target.value);
  };

  const handleTaskClick = (task) => {
    setSelectedTasks(selectedTasks.filter(t => t !== task));
  };

  const createInterview = () => {
    if (!interviewName) {
      setError('Please enter interview name');
      return;
    }

    axios.post('http://0.0.0.0:8000/interview/create_interview', {
      name: interviewName,
      tasks: selectedTasks
    })
      .then(response => {
        console.log('Interview created successfully:', response.data);
      })
      .catch(error => {
        console.error('Error creating interview:', error);
      });
  };

  return (
    <div className="constructor-container">
      <h1>Create Interview</h1>
      <input
        type="text"
        placeholder="Enter interview name"
        value={interviewName}
        onChange={handleInputChange}
        className="interview-input"
      />
      {error && (
        <div className="error-popup">{error}</div>
      )}
      <div className="drop-zone"
        onDrop={handleDrop}
        onDragOver={(e) => e.preventDefault()}>
        {selectedTasks.map(task => (
          <div
            key={task.name}
            className="selected-task"
            style={{ backgroundColor: task.color }}
            onClick={() => handleTaskClick(task)}>
            {task.name}
          </div>
        ))}
      </div>
      <div className="task-list-container" ref={taskListRef}>
        <div className="task-list">
          {tasks.map((task, index) => (
            <div
              key={task.name}
              className="task"
              draggable
              onDragStart={(e) => handleDragStart(e, task)}>
              {task.name ? task.name : "No Name"}
            </div>
          ))}
        </div>
      </div>
      {selectedTasks.length > 0 && (
        <button onClick={createInterview}>Create Interview</button>
      )}
    </div>
  );
};

export default ConstructorPage;

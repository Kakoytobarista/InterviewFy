import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import './InterviewPage.css';

function InterviewPage() {
  const { interview_id } = useParams();
  const [interviewName, setInterviewName] = useState('');
  const [tasks, setTasks] = useState([]);
  const [currentTaskIndex, setCurrentTaskIndex] = useState(0);
  const [taskPassed, setTaskPassed] = useState(false);
  const navigate = useNavigate();

  useEffect(() => {
    if (!interview_id) {
      navigate('/');
      return;
    }

    const storedTasks = localStorage.getItem('tasks');
    if (storedTasks) {
      try {
        const parsedTasks = JSON.parse(storedTasks);
        setTasks(parsedTasks);
      } catch (error) {
        console.error('Error parsing tasks from localStorage:', error);
      }
    }

    fetchInterviewData();
  }, [interview_id, navigate]);

  const fetchInterviewData = async () => {
    try {
      const storedInterviews = localStorage.getItem('interviews');
      if (storedInterviews) {
        const parsedInterviews = JSON.parse(storedInterviews);
        const interview = parsedInterviews.find(interview => interview.id === parseInt(interview_id));
        if (interview) {
          setInterviewName(interview.name);
        } else {
          console.error('Interview not found');
        }
      } else {
        console.error('No interviews found in localStorage');
      }
    } catch (error) {
      console.error('Error fetching interview data:', error);
    }
  };

  const continueInterview = async () => {
    if (currentTaskIndex < tasks.length - 1) {
      setCurrentTaskIndex(prevIndex => prevIndex + 1);
    } else {
      navigate(`/interview/${interview_id}/done`);
    }

    const interview_status_id = localStorage.getItem('interview_status_id');
    let score = parseInt(localStorage.getItem('score'));
    let updatedScore = taskPassed ? score + 1 : score;

    try {
      const response = await fetch(`http://0.0.0.0:8000/intreview_status/update_interview_status/${interview_status_id}`, {
        method: 'PATCH',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          task_passed: taskPassed,
          score: updatedScore
        })
      });

      if (response.ok) {
        localStorage.setItem('score', updatedScore.toString());
        console.log('Score updated successfully');
      } else {
        console.error('Failed to update score');
      }
    } catch (error) {
      console.error('Error updating score:', error);
    }
  };

  return (
    <div className="interview-page-container">
      <div className="interview-header">
        <h1 className="interview-page-heading">{interviewName}</h1>
      </div>
      {tasks.length > 0 ? (
        <div className="interview-task-container">
          <div className="interview-task-left">
            <h2 className="interview-task-heading">{tasks[currentTaskIndex].name}</h2>
            <p className="interview-task-content">{tasks[currentTaskIndex].content}</p>
          </div>
          <div className="interview-task-right">
            <textarea className="code-input" placeholder="Enter your code here"></textarea>
          </div>
        </div>
      ) : (
        <p>Loading...</p>
      )}
      <div className="interview-buttons-container">
        <div className="interview-checkbox-container">
          <label className="interview-checkbox-label">
            <input type="checkbox" checked={taskPassed} onChange={() => setTaskPassed(!taskPassed)} />
            Passed
          </label>
        </div>
        <button className="interview-button" onClick={continueInterview}>Next</button>
      </div>
    </div>
  );
}

export default InterviewPage;

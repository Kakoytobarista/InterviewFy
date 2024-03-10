import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import './SelectInterviewPage.css';

function SelectInterviewPage() {
  const [interviews, setInterviews] = useState([]);
  const [selectedInterview, setSelectedInterview] = useState('');
  const [candidateName, setCandidateName] = useState('');
  const navigate = useNavigate();

  useEffect(() => {
    fetchInterviews();
    clearLocalStorage();
  }, []);

  const fetchInterviews = async () => {
    try {
      const response = await fetch('http://0.0.0.0:8000/interview/get_all');
      const data = await response.json();
      setInterviews(data.interviews); // Предположим, что данные приходят в формате { interviews: [...] }

      localStorage.setItem('interviews', JSON.stringify(data.interviews));
    } catch (error) {
      console.error('Error fetching interviews:', error);
    }
  };

  const clearLocalStorage = () => {
    const keys = Object.keys(localStorage);
    const interviewKeys = keys.filter(key => key !== 'interviews');
    interviewKeys.forEach(key => {
      localStorage.removeItem(key);
    });
  };

  const startInterview = async () => {
    try {
      console.log('Selected Interview:', selectedInterview);
      console.log('Candidate Name:', candidateName);
      if (!selectedInterview || !candidateName) {
        console.error('Please select an interview and enter candidate name.');
        return;
      }

      const startInterviewResponse = await fetch('http://0.0.0.0:8000/interview_process/start_interview', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          interview_id: selectedInterview,
          full_name: candidateName,
        }),
      });

      if (startInterviewResponse.ok) {
        const responseData = await startInterviewResponse.json();
        const { user_id } = responseData;
        const { id } = responseData;
        const { score } = responseData;

        localStorage.setItem('selectedInterviewName', selectedInterview);
        localStorage.setItem('user_id', user_id);
        localStorage.setItem('interview_status_id', id);
        localStorage.setItem('score', score);

        const taskResponse = await fetch(`http://0.0.0.0:8000/task/get_all/${selectedInterview}`);
        const taskData = await taskResponse.json();

        console.log('Tasks data:', taskData);
        localStorage.setItem('tasks', JSON.stringify(taskData.tasks));
        localStorage.setItem('candidateName', candidateName);

        navigate(`/interview/${selectedInterview}/start`);
      } else {
        console.error('Failed to start interview');
      }
    } catch (error) {
      console.error('Error starting interview:', error);
    }
  };

  return (
    <div className="select-interview-container">
      <h1 className="select-interview-heading">Interview<span>Fy</span></h1>
      <div className="select-interview-form">
        <select
          className="select-interview-dropdown"
          value={selectedInterview}
          onChange={(e) => setSelectedInterview(e.target.value)}
        >
          <option value="">Select an interview</option>
          {interviews.map((interview) => (
            <option key={interview.id} value={interview.id}>
              {interview.name}
            </option>
          ))}
        </select>
        <input
          className="select-interview-input"
          type="text"
          value={candidateName}
          onChange={(e) => setCandidateName(e.target.value)}
          placeholder="Candidate Name"
        />
        <button className="select-interview-button" onClick={startInterview}>
          START
        </button>
      </div>
    </div>
  );
}

export default SelectInterviewPage;

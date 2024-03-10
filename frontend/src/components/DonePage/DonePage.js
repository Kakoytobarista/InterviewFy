import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import './DonePage.css';

function DonePage() {
  const { interview_name } = useParams();
  const [candidateName, setCandidateName] = useState('');
  const [storedScore, setStoredScore] = useState(null);
  const [tasks, setTasks] = useState(0);

  useEffect(() => {
    const fetchData = async () => {
      const candidateNameFromLocalStorage = localStorage.getItem('candidateName');
      const tasksFromLocalStorage = localStorage.getItem('tasks');
      const storedScoreFromLocalStorage = localStorage.getItem('score');

      // Ждем, пока все данные из localStorage загрузятся
      if (candidateNameFromLocalStorage && tasksFromLocalStorage && storedScoreFromLocalStorage) {
        setCandidateName(candidateNameFromLocalStorage);
        setTasks(tasksFromLocalStorage ? JSON.parse(tasksFromLocalStorage).length : 0);
        setStoredScore(storedScoreFromLocalStorage);

        // Отправка сообщения в Telegram
        sendAlertToTelegram();
      }
    };

    fetchData();
  }, []);

const sendAlertToTelegram = async () => {
  let alertText = `
  Successfully finished *${interview_name}* interview with *${candidateName}* with score *${storedScore}* from *${tasks}*
  `;
  console.log(alertText)
  try {
    const response = await fetch('http://0.0.0.0:8000/alert/send_alert', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ text: alertText }),
    });
    if (!response.ok) {
      console.error('Failed to send alert to Telegram channel');
    }
  } catch (error) {
    console.error('Error sending alert to Telegram channel:', error);
  }
};

  return (
    <div className="done-page-container">
      <h3 className="done-page-heading">Successfully finished <strong>{interview_name}</strong> interview with <strong>{candidateName}</strong> with score <strong>{storedScore}</strong> from <strong>{tasks}</strong></h3>
    </div>
  );
}

export default DonePage;

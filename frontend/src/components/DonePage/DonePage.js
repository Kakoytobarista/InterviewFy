import React from 'react';
import { useParams } from 'react-router-dom';
import './DonePage.css';

function DonePage() {
  const { interview_name, candidate_name } = useParams();
  let candidateName = localStorage.getItem('candidateName')

  console.log(interview_name)

  const storedScore = localStorage.getItem('score');

  const tasks = JSON.parse(localStorage.getItem('tasks')).length;

  return (
    <div className="done-page-container">
      <h3 className="done-page-heading">Successfully finished <strong>{interview_name}</strong>
        interview with <strong>{candidateName}</strong> with
        score <strong>{storedScore}</strong> from <strong>{tasks}</strong></h3>
    </div>
  );
}

export default DonePage;

import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import SelectInterviewPage from './components/SelectInterviewPage/SelectInterviewPage';
import InterviewPage from './components/InterviewPage/InterviewPage';
import DonePage from './components/DonePage/DonePage';

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/interview/:interview_id/start" element={<InterviewPage action="start" />} />
          <Route path="/interview/:interview_id/done" element={<DonePage />} />
          <Route path="/interview/select" element={<SelectInterviewPage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;

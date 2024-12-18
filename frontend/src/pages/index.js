import React, { useState } from 'react';

const PythonCompiler = () => {
  const [code, setCode] = useState('');
  const [output, setOutput] = useState('');
  const [error, setError] = useState('');

  const runCode = async () => {
    try {
      const response = await fetch('http://localhost:5000/run', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ code }),
      });
      const data = await response.json();
      setOutput(data.output || '');
      setError(data.error || '');
    } catch (err) {
      setError('Failed to connect to the server');
    }
  };

  return (
    <div>
      <textarea
        value={code}
        onChange={(e) => setCode(e.target.value)}
        placeholder="Write your Python code here..."
      />
      <button onClick={runCode}>Run</button>
      <h3>Output</h3>
      <pre>{output}</pre>
      <h3>Error</h3>
      <pre>{error}</pre>
    </div>
  );
};

export default PythonCompiler;

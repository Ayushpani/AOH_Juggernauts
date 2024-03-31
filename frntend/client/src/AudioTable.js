import React, { useState } from 'react';
import './Audiotable.css'

function AudioTable() {
  const [audioFiles, setAudioFiles] = useState([]);
  const [customer, setCustomer] = useState('');
  const [employee, setEmployee] = useState('');

  const generateRandomName = () => {
    const customers = ['Alice', 'Bob', 'Charlie', 'Diana', 'Ethan', 'Fiona'];
    const employees = ['George', 'Hannah', 'Isaac', 'Julia', 'Kevin', 'Linda'];

    const randomCustomer = customers[Math.floor(Math.random() * customers.length)];
    const randomEmployee = employees[Math.floor(Math.random() * employees.length)];

    setCustomer(randomCustomer);
    setEmployee(randomEmployee);
  };

  const handleFileUpload = (event) => {
    const files = event.target.files;
    const newAudioFiles = [];

    for (let i = 0; i < files.length; i++) {
      if (files[i].type === 'audio/wav') {
        newAudioFiles.push(files[i]);
      }
    }

    setAudioFiles(newAudioFiles);

    // Generate random names when files are uploaded
    generateRandomName();
  };

  return (
    <div>
      <h2>Upload WAV Files</h2>
      <input type="file" accept="audio/wav" onChange={handleFileUpload} multiple />

      {audioFiles.length > 0 && (
        <table>
          <thead>
            <tr>
              <th>Customer</th>
              <th>Employee</th>
              <th>Audio</th>
            </tr>
          </thead>
          <tbody>
            {audioFiles.map((file, index) => (
              <tr key={index}>
                <td>
                  <input type="text" value={customer} onChange={(e) => setCustomer(e.target.value)} />
                </td>
                <td>
                  <input type="text" value={employee} onChange={(e) => setEmployee(e.target.value)} />
                </td>
                <td>
                  <audio controls>
                    <source src={URL.createObjectURL(file)} type="audio/wav" />
                  </audio>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}

export default AudioTable;

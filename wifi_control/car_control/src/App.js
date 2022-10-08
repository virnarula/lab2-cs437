import './App.css';
import io from "socket.io-client";
import React, {useEffect, useState} from 'react';

const socket = io("192.168.10.95:8080");

function App() {
  const [cpu_temperature, set_cpu_temperature] = useState(0)
  const [gpu_temperature, set_gpu_temperature] = useState(0)
  const [cpu_usage, set_cpu_usage] = useState(0)

  const sendInstruction = (instruction) => {
    console.log(instruction)
    socket.emit('instruction', {instruction});
  }

  useEffect(() => {
    // subscribe to socket events
    socket.on("data", (data)=>{
      set_cpu_temperature(data['cpu_temperature'])
      set_gpu_temperature(data['gpu_temperature'])
      set_cpu_usage(data['cpu_usage'])
    }); 
  });

  useEffect(() => {
    const keyDownHandler = event => {
      event.preventDefault();
      if (event.key === 'w') {
        sendInstruction("forward")
      } else if (event.key === 'a') {
        sendInstruction("left")
      } else if (event.key === 's') {
        sendInstruction("backward")
      } else if (event.key === 'd') {
        sendInstruction("right")
      } else {
        sendInstruction("stop")
      }
    };
    document.addEventListener('keydown', keyDownHandler);

    const getCarData = setInterval(() => {
      socket.emit('get_car_data')
    }, 1000);

    return () => {
      document.removeEventListener('keydown', keyDownHandler);
      clearInterval(getCarData)
    };
  }, []);

  return (
    <div className="App">
      <div className="car_info">
        <h2>Car Information</h2>
        <p id="cpu_temperature">CPU Temperature: {cpu_temperature}</p>
        <p id="gpu_temperature">GPU Temperature: {gpu_temperature}</p>
        <p id="cpu_usage">CPU Usage: {cpu_usage}</p>
      </div>
    </div>
  );
}

export default App;

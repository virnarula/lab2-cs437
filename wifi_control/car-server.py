from aiohttp import web
import socketio
# import time
import picar_4wd as fc

sio = socketio.AsyncServer(cors_allowed_origins='*')
app = web.Application()
sio.attach(app)

@sio.event
async def connect(sid, environ, auth):
    print('Connected to', sid)

@sio.event
async def instruction(sid, data):
    print("Socket ID: " , sid, " Instruction: ", data)
    if data['instruction']:
        instruction = data['instruction']
    if instruction == 'forward':
        fc.forward(50)
    elif instruction == 'left':
        fc.turn_left(50)
    elif instruction == 'backward':
        fc.backward(50)
    elif instruction == 'right':
        fc.turn_right(50)
    elif instruction == 'stop':
        fc.stop()
    else:
        fc.stop()

@sio.event
async def get_car_data(sid):
    print('Sending data to ', sid)
    data = {
        "cpu_temperature": str(fc.cpu_temperature()),
        "gpu_temperature": str(fc.gpu_temperature()),
        "cpu_usage": fc.cpu_usage()
    }
    await sio.emit('data', data)

@sio.event
async def disconnet(sid):
    print('Disconnected from', sid)


## We kick off our server
if __name__ == '__main__':
    web.run_app(app)
    
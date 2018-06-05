import sys
import chat

app = create_app(debug=True)

if __name__ == '__main__':
    socketio.run(app)

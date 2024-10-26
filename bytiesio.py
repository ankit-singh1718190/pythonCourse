import io
buffer = io.BytesIO()
buffer.write(b'Hello, this is in memory!')
buffer.seek(0)  # Go back to the beginning of the buffer
print(buffer.read())  # Outputs: b'Hello, this is in memory!'

import pyaudio
import wave

def record_audio(filename, duration=5, rate=44100, channels=1):
    # Configuração do PyAudio
    p = pyaudio.PyAudio()

    # Configurações de gravação
    stream = p.open(format=pyaudio.paInt16, 
                    channels=channels,
                    rate=rate,
                    input=True,
                    frames_per_buffer=1024)

    print("Gravando...")

    frames = []

    # Gravação do áudio
    for i in range(0, int(rate / 1024 * duration)):
        data = stream.read(1024)
        frames.append(data)

    print("Gravação finalizada.")

    # Parando a gravação
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Salvando o áudio em um arquivo WAV
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
        wf.setframerate(rate)
        wf.writeframes(b''.join(frames))

# Exemplo de uso
record_audio("output.wav", duration=5)
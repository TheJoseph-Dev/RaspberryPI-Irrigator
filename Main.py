from Models.Irrigador import Irrigador

if __name__ == "__main__":
    irrigador = Irrigador()
    Irrigador.print_name()
    irrigador.run()
    #TODO: Deploy a Streamlit or ThingsBoard with real-time data update
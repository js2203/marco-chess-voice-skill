from mycroft import MycroftSkill, intent_file_handler


class MarcoChessVoice(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('voice.chess.marco.intent')
    def handle_voice_chess_marco(self, message):
        self.speak_dialog('voice.chess.marco')


def create_skill():
    return MarcoChessVoice()


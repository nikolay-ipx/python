class Viber:
    mes_veb_list = {}

    @classmethod
    def add_message(cls, msg):
        cls.mes_veb_list[id(msg)] = msg

    @classmethod
    def remove_message(cls, msg):
        cls.mes_veb_list.pop(id(msg))

    @classmethod
    def set_like(cls, msg):
        msg.fl_like = not msg.fl_like

    @classmethod
    def show_last_message(cls, msg):
        for i in tuple(cls.mes_veb_list.values())[-msg:]:
            print(i.text)

    @classmethod
    def total_messages(cls):
        return len(cls.mes_veb_list)

class Message:
    def __init__(self, text, fl_like = False):
        self.text = text
        self.fl_like = fl_like


msg = Message("Всем привет!")
Viber.add_message(msg)
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))
Viber.set_like(msg)
Viber.remove_message(msg)
Viber.show_last_message(2)
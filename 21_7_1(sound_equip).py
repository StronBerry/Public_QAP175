class SoundEquipment:
    def switch_on(self):
        self.state = True

    def switch_off(self):
        self.state = False


class Microphone(SoundEquipment):
    def __init__(self, volume=0, state=False):
        self.volume = max(0, min(volume, 10))  # Ограничение громкости от 0 до 10
        self.state = state  # Установка начального состояния (включен/выключен)

    def adjust_volume(self, volume):
        # Изменяем громкость и ограничиваем её в пределах от 0 до 10
        self.volume = max(0, min(volume, 10))
        print(f"Volume is now {self.volume}")


class Speaker(SoundEquipment):
    def __init__(self, bass=0, state=False):
        self.bass = max(0, min(bass, 10))  # Ограничение басов от 0 до 10
        self.state = state  # Установка начального состояния (включен/выключен)

    def adjust_bass(self, bass):
        # Изменяем уровень басов и ограничиваем его в пределах от 0 до 10
        self.bass = max(0, min(bass, 10))
        print(f"Bass level is now {self.bass}")

# Создаём объект микрофон с громкостью 5 состоянием "включен"
mic = Microphone(volume=5, state=True)
# Отключаем микрофон
mic.switch_off()
# Устанавливаем новый уровень громкости
mic.adjust_volume(7)

# Создаём объект динамик с уровнем басов 7 и состоянием "выключен"
sp = Speaker(7, False)
# Включаем динамик
sp.switch_on()
# Устанавливаем новый уровень басов
sp.adjust_bass(8)


from responsive_voice import ResponsiveVoice
from responsive_voice.voices import PortugueseBrazil

#pt = PortugueseBrazil()
#pt.say('E ai, mano brown')

engine = ResponsiveVoice(lang=ResponsiveVoice.PORTUGUESE_BR, rate=0.90) #rate é a velocidade, variando de 0 a 1
engine.say('Hello')






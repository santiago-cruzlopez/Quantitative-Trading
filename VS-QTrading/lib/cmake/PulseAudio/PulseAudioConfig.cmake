set(PULSEAUDIO_FOUND TRUE)

set(PULSEAUDIO_VERSION_MAJOR 17)
set(PULSEAUDIO_VERSION_MINOR 0)
set(PULSEAUDIO_VERSION 17.0)
set(PULSEAUDIO_VERSION_STRING "17.0")

find_path(PULSEAUDIO_INCLUDE_DIR pulse/pulseaudio.h HINTS "/home/santi_cruz/Documents/Quantitative-Trading/VS-QTrading/include")
find_library(PULSEAUDIO_LIBRARY NAMES pulse libpulse HINTS "/home/santi_cruz/Documents/Quantitative-Trading/VS-QTrading/lib")
find_library(PULSEAUDIO_MAINLOOP_LIBRARY NAMES pulse-mainloop-glib libpulse-mainloop-glib HINTS "/home/santi_cruz/Documents/Quantitative-Trading/VS-QTrading/lib")

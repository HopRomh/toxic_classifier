
from PyQt6.QtGui import QPalette, QColor

themes = {}

# light_palette
light_palette = QPalette()
light_palette.setColor(QPalette.ColorRole.Window, QColor(240, 240, 245))
light_palette.setColor(QPalette.ColorRole.WindowText, QColor(30, 30, 30))
light_palette.setColor(QPalette.ColorRole.Base, QColor(255, 255, 255))
light_palette.setColor(QPalette.ColorRole.Text, QColor(10, 10, 10))
light_palette.setColor(QPalette.ColorRole.Button, QColor(200, 220, 240))
light_palette.setColor(QPalette.ColorRole.ButtonText, QColor(10, 10, 10))
light_palette.setColor(QPalette.ColorRole.Highlight, QColor(100, 150, 220))
light_palette.setColor(QPalette.ColorRole.HighlightedText, QColor(255, 255, 255))
themes["Светлая"] = light_palette

# dark_palette
dark_palette = QPalette()
dark_palette.setColor(QPalette.ColorRole.Window, QColor(18, 18, 30))
dark_palette.setColor(QPalette.ColorRole.WindowText, QColor(230, 230, 240))
dark_palette.setColor(QPalette.ColorRole.Base, QColor(28, 28, 40))
dark_palette.setColor(QPalette.ColorRole.Text, QColor(220, 220, 230))
dark_palette.setColor(QPalette.ColorRole.Button, QColor(40, 50, 70))
dark_palette.setColor(QPalette.ColorRole.ButtonText, QColor(230, 230, 240))
dark_palette.setColor(QPalette.ColorRole.Highlight, QColor(90, 120, 200))
dark_palette.setColor(QPalette.ColorRole.HighlightedText, QColor(255, 255, 255))
themes["Тёмная"] = dark_palette

#castom_palette
castom_palette = QPalette()
castom_palette.setColor(QPalette.ColorRole.Window, QColor(25, 30, 40))       
castom_palette.setColor(QPalette.ColorRole.WindowText, QColor(200, 210, 220)) 
castom_palette.setColor(QPalette.ColorRole.Base, QColor(35, 40, 55))          
castom_palette.setColor(QPalette.ColorRole.Text, QColor(255, 255, 255))      
castom_palette.setColor(QPalette.ColorRole.Button, QColor(50, 60, 80))      
castom_palette.setColor(QPalette.ColorRole.ButtonText, QColor(200, 210, 220)) 
castom_palette.setColor(QPalette.ColorRole.Highlight, QColor(70, 90, 130))    
castom_palette.setColor(QPalette.ColorRole.HighlightedText, QColor(230, 230, 240)) 

# Синяя тема
blue_palette = QPalette()
blue_palette.setColor(QPalette.ColorRole.Window, QColor(20, 30, 60))
blue_palette.setColor(QPalette.ColorRole.WindowText, QColor(200, 220, 255))
blue_palette.setColor(QPalette.ColorRole.Base, QColor(30, 45, 90))
blue_palette.setColor(QPalette.ColorRole.Text, QColor(220, 240, 255))
blue_palette.setColor(QPalette.ColorRole.Button, QColor(50, 70, 120))
blue_palette.setColor(QPalette.ColorRole.ButtonText, QColor(200, 220, 255))
blue_palette.setColor(QPalette.ColorRole.Highlight, QColor(100, 150, 200))
blue_palette.setColor(QPalette.ColorRole.HighlightedText, QColor(255, 255, 255))
themes["Синяя"] = blue_palette

# Темно желтая
contrast_palette = QPalette()
contrast_palette.setColor(QPalette.ColorRole.Window, QColor(0, 0, 0))
contrast_palette.setColor(QPalette.ColorRole.WindowText, QColor(255, 255, 0))
contrast_palette.setColor(QPalette.ColorRole.Base, QColor(20, 20, 20))
contrast_palette.setColor(QPalette.ColorRole.Text, QColor(255, 255, 0))
contrast_palette.setColor(QPalette.ColorRole.Button, QColor(50, 50, 50))
contrast_palette.setColor(QPalette.ColorRole.ButtonText, QColor(255, 255, 0))
contrast_palette.setColor(QPalette.ColorRole.Highlight, QColor(255, 0, 0))
contrast_palette.setColor(QPalette.ColorRole.HighlightedText, QColor(255, 255, 255))
themes["Темно желтая"] = contrast_palette

# Зелёная тема
green_palette = QPalette()
green_palette.setColor(QPalette.ColorRole.Window, QColor(25, 40, 25))
green_palette.setColor(QPalette.ColorRole.WindowText, QColor(200, 255, 200))
green_palette.setColor(QPalette.ColorRole.Base, QColor(30, 50, 30))
green_palette.setColor(QPalette.ColorRole.Text, QColor(220, 255, 220))
green_palette.setColor(QPalette.ColorRole.Button, QColor(50, 70, 50))
green_palette.setColor(QPalette.ColorRole.ButtonText, QColor(200, 255, 200))
green_palette.setColor(QPalette.ColorRole.Highlight, QColor(100, 200, 100))
green_palette.setColor(QPalette.ColorRole.HighlightedText, QColor(255, 255, 255))
themes["Зелёная"] = green_palette



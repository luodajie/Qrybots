def group_box_style(groupbox=None):
    groupbox.setStyleSheet('''QGroupBox {
                            border: 1px solid gray;
                            border-radius: 9px;
                            margin-top: 8em;
                            margin-bottom: 2em;
                            padding: 10px;
                            font-size: 12px;
                            font-weight: bold;
                        }
                        
                        QGroupBox::title {
                            margin-top: 2.5em;
                            subcontrol-origin: margin;
                            left: 5em;
                            padding-left: 4em;
                            font-size: 12em;
                            font-weight: bold;

                        }''')


def run_button_style(button=None):
    button.setStyleSheet('''
                
                                            QPushButton:open { /* when the button has its menu open */
                                background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                                                  stop: 0 #dadbde, stop: 1 #f6f7fa);
                            }
                            
                            QPushButton::menu-indicator {
                                image: url(menu_indicator.png);
                                subcontrol-origin: padding;
                                subcontrol-position: bottom right;
                            }
                            
                            QPushButton::menu-indicator:pressed, QPushButton::menu-indicator:open {
                                position: relative;
                                top: 2px; left: 2px; /* shift the arrow by 2 px */
                            }
    ''')

from main import *
from dialog import *
import sys
import pickle
import os
from datetime import datetime

FILE_NAME = "data.txt"

QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)


class Event:
    def __init__(self, date, name, description, object_name=None, **kwargs):
        self.__date = date
        self.__object_name = object_name
        self.__event_name = name
        self.__event_description = description
        self.__time = kwargs["time"]
        self.__duration = kwargs["duration"]
        self.__place = kwargs["place"]

    def get_event(self):
        """Saves dictionary to list"""
        return Event(self.__date, self.__event_name, self.__event_description, time=self.__time,
                     duration=self.__duration, place=self.__place)

    def set_date(self, new_date):
        self.__date = new_date

    def set_event_name(self, new_event_name):
        self.__event_name = new_event_name

    def set_description(self, new_description):
        self.__event_description = new_description

    def set_time(self, new_time):
        self.__time = new_time

    def set_duration(self, new_duration):
        self.__duration = new_duration

    def set_place(self, new_place):
        self.__place = new_place

    def get_date(self):
        return self.__date

    def get_object_name(self):
        return self.__object_name

    def get_event_name(self) -> str:
        return self.__event_name

    def get_description(self) -> str:
        return self.__event_description

    def get_time(self):
        return self.__time

    def get_date_time(self):
        return QDateTime(self.__date, self.__time)

    def get_duration(self):
        return self.__duration

    def get_place(self):
        return self.__place


class EventContainer:
    __events: list[Event] = []

    @staticmethod
    def sort_events():
        EventContainer.__events.sort(key=lambda event: event.get_time())
        EventContainer.__events.sort(key=lambda event: event.get_date())

    @staticmethod
    def remove_data(data_to_remove):
        return EventContainer.__events.remove(data_to_remove)

    @staticmethod
    def set_data(data):
        EventContainer.__events.append(data)

    @staticmethod
    def get_events():
        return EventContainer.__events

    @staticmethod
    def add_reminder():
        try:
            EventContainer.sort_events()
            first_event = EventContainer.get_events()[0]
            event_name = first_event.get_event_name()
            event_obj = first_event.get_object_name()
            event_description = first_event.get_description()
            dt = f"{first_event.get_date().toString('dd/MM/yyyy')}"
            tm = f"{first_event.get_time().toString('hh:mm')}"
            event_reminder = f"/C TITLE {event_name}&ECHO {event_name}&ECHO.&ECHO {tm} {dt} {event_description}.&TIMEOUT -1"
            os.system(
                f'schtasks /create /F /tn "{event_obj}" /tr "cmd {event_reminder}" /ed "{dt}" /et "{tm}" /sc HOURLY')
        except IndexError:
            pass

    @staticmethod
    def remove_reminder(event_data):
        for event in EventContainer.__events:
            if event == event_data:
                os.system(f'schtasks /delete /F /tn "{event.get_object_name()}"')
                EventContainer.remove_data(event)


class MainWindow(QMainWindow):
    __button_objects = {}

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.addEventButton.clicked.connect(self.__open_creating_dialog)
        self.ui.calendarWidget.setLocale(QLocale.Ukrainian)
        self.ui.calendarWidget.selectionChanged.connect(self.check_event)
        self.ui.calendarWidget.selectionChanged.connect(self.__check_date)
        self.noEventLabel = QLabel(self.ui.groupBox)
        self.noEventLabel.setGeometry(QRect(100, 100, 120, 61))
        self.noEventLabel.setAlignment(Qt.AlignCenter)
        self.font = QFont()
        self.font.setItalic(True)
        self.noEventLabel.setFont(self.font)
        self.noEventLabel.setText("В цю дату нічого не заплановано")
        self.__calc_days_to_event()

    def __check_date(self):
        """Checks if selected date whether selected date is less than current"""
        now_date = QDate(int(datetime.now().strftime("%Y")), int(datetime.now().strftime("%m")),
                         int(datetime.now().strftime("%d")))
        if self.ui.calendarWidget.selectedDate() < now_date:
            self.ui.addEventButton.setDisabled(True)
        else:
            self.ui.addEventButton.setDisabled(False)

    def check_event(self):
        """Checks events by the data, if there are no events at that day, places noEventLabels"""
        for obj in MainWindow.__button_objects:
            self.ui.verticalLayout_3.removeWidget(obj)
            obj.deleteLater()
        MainWindow.__button_objects.clear()
        self.ui.verticalLayout_3.addWidget(self.noEventLabel)
        new_date = self.ui.calendarWidget.selectedDate()
        for event in EventContainer.get_events():
            if event.get_date() == new_date:
                self.ui.verticalLayout_3.removeWidget(self.noEventLabel)
                event_button = QPushButton()
                event_button.setGeometry(QRect(100, 100, 120, 61))
                event_button.setText(f"{event.get_event_name()} - {event.get_time().toString('hh:mm')}")
                self.ui.verticalLayout_3.addWidget(event_button)
                MainWindow.__button_objects[event_button] = event

        for button in MainWindow.__button_objects:
            button.clicked.connect(self.__open_changing_dialog)

    def __calc_days_to_event(self):
        """Calculates days to the nearest event"""
        EventContainer.sort_events()
        try:
            now_date = QDate(int(datetime.now().strftime("%Y")), int(datetime.now().strftime("%m")),
                             int(datetime.now().strftime("%d")))
            d2 = EventContainer.get_events()[0].get_date()
            delta_d = now_date.daysTo(d2)
            self.ui.timeToEventLabel.setText(f"Кіл-сть днів до найближчого заходу: {delta_d}")
        except IndexError:
            self.ui.timeToEventLabel.setText(f"Кіл-сть днів до найближчого заходу: --")

    def __open_creating_dialog(self):
        """Opens dialog window for creating event"""
        dial_to_create = CreatorDialogWindow(date=self.ui.calendarWidget.selectedDate())
        dial_to_create.exec_()
        self.check_event()
        self.__calc_days_to_event()

    def __open_changing_dialog(self):
        """Opens dialog window for changing event"""
        butt_obj = QObject.sender(self)
        dial_to_change = ChangerDialogWindow(event=MainWindow.__button_objects[butt_obj])
        dial_to_change.exec_()
        self.check_event()
        self.__calc_days_to_event()


class DialogWindow(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.dialog = Ui_Dialog()
        self.dialog.setupUi(self)
        self.dialog.saveButton.clicked.connect(self._save_event)
        self.dialog.hourSpin.valueChanged.connect(self.__set_minimum_time)
        self.error_message = QLabel()
        self.error_message.setObjectName("errorMessage")
        self.error_message.setStyleSheet("#errorMessage {color: red;}")

    def __set_minimum_time(self):
        if self.dialog.hourSpin.value() == int(datetime.now().strftime("%H")):
            self.dialog.minuteSpin.setMinimum(int(datetime.now().strftime("%M")))
        else:
            self.dialog.minuteSpin.setMinimum(0)


class CreatorDialogWindow(DialogWindow):
    def __init__(self, date=None, parent=None):
        DialogWindow.__init__(self, parent)
        self.__date = date
        self.__time_spins_installation()

    def __time_spins_installation(self):
        date_params = [int(i) for i in datetime.now().strftime("%Y %m %d").split()]
        if self.__date == QDate(*date_params):
            self.dialog.hourSpin.setMinimum(int(datetime.now().strftime("%H")))
            self.dialog.minuteSpin.setMinimum(int(datetime.now().strftime("%M")))

    def __check_event_time(self, event_time, curr_hour, curr_minute):
        date_params = [int(i) for i in datetime.now().strftime("%Y %m %d").split()]
        if self.__date == QDate(*date_params):
            if (event_time.hour() < curr_hour) or (
                    event_time.hour() == curr_hour and event_time.minute() <= curr_minute):
                self.error_message.setText("*значення часу повинно бути більше теперішнього")
                self.dialog.verticalLayout_6.addWidget(self.error_message)
                return False
        return True

    def __check_event_name(self):
        if self.dialog.eventName.text() == "":
            self.error_message.setText("*введіть назву заходу")
            self.dialog.verticalLayout_5.addWidget(self.error_message)
            return False
        return True

    def __check_crossing_with_previous_event(self, event_obj):
        if event_obj != EventContainer.get_events()[0]:
            # if this event is not first, then we get previous event by index current one - 1
            curr_event_ind = EventContainer.get_events().index(event_obj)
            previous_event = EventContainer.get_events()[curr_event_ind - 1]
            previous_event_duration = previous_event.get_duration()[0]
            if previous_event.get_duration()[1] == 0:
                previous_event_duration *= 3600000
            else:
                previous_event_duration *= 60000
            if previous_event_duration >= previous_event.get_date_time().msecsTo(event_obj.get_date_time()):
                self.error_message.setText("Ця подія перетинається з минулою")
                self.dialog.verticalLayout.addWidget(self.error_message)
                EventContainer.remove_data(event_obj)
                return False
        return True

    def __check_crossing_with_next_event(self, event_obj):
        if event_obj != EventContainer.get_events()[-1]:
            # if this event is not last, then we get previous event by index current one + 1
            curr_event_ind = EventContainer.get_events().index(event_obj)
            next_event = EventContainer.get_events()[curr_event_ind + 1]
            event_duration = event_obj.get_duration()[0]
            if event_obj.get_duration()[1] == 0:
                event_duration *= 3600000
            else:
                event_duration *= 60000
            if event_duration >= event_obj.get_date_time().msecsTo(next_event.get_date_time()):
                self.error_message.setText("Ця подія перетинається з наступною")
                self.dialog.verticalLayout.addWidget(self.error_message)
                EventContainer.remove_data(event_obj)
                return False
        return True

    def _save_event(self):
        if not self.__check_event_name():
            return
        event_text = self.dialog.eventName.text()
        event_descript = self.dialog.eventDescription.toPlainText()
        curr_hour, curr_minute = int(datetime.now().strftime("%H")), int(datetime.now().strftime("%M"))
        event_time = QTime(self.dialog.hourSpin.value(), self.dialog.minuteSpin.value())
        if not self.__check_event_time(event_time, curr_hour, curr_minute):
            return
        event_duration = [self.dialog.durationSpin.value(), self.dialog.comboBoxDuration.currentIndex()]
        event_place = self.dialog.placeEdit.text()
        event_obj = Event(self.__date, event_text, event_descript, object_name=event_text, time=event_time,
                          duration=event_duration,
                          place=event_place)
        EventContainer.set_data(event_obj)
        EventContainer.sort_events()
        if not self.__check_crossing_with_previous_event(event_obj):
            return
        if not self.__check_crossing_with_next_event(event_obj):
            return
        EventContainer.add_reminder()
        self.accept()


class ChangerDialogWindow(DialogWindow):
    def __init__(self, event, parent=None):
        DialogWindow.__init__(self, parent)
        self._event = event
        self.current_date = QDate(int(datetime.now().strftime("%Y")), int(datetime.now().strftime("%m")),
                                  int(datetime.now().strftime("%d")))
        self.dialog.saveButton.setText("Змінити захід")
        self.deleteButton = QPushButton()
        self.deleteButton.setText("Видалити захід")
        font_for_btn = QFont()
        font_for_btn.setFamily(u"Segoe UI Historic")
        font_for_btn.setPointSize(10)
        font_for_btn.setBold(True)
        font_for_btn.setWeight(75)
        self.deleteButton.setFont(font_for_btn)
        self.deleteButton.clicked.connect(self.__delete_event)
        self.dialog.verticalLayout_4.addWidget(self.deleteButton)
        self.date_box = QGroupBox()
        font_for_date_box = QFont()
        font_for_date_box.setPointSize(10)
        font_for_date_box.setBold(True)
        font_for_date_box.setWeight(75)
        self.date_box.setTitle("Дата")
        self.date_box.setFont(font_for_date_box)
        self.dialog.verticalLayout_3.addWidget(self.date_box)
        self.horizontalLayout_for_date = QHBoxLayout(self.date_box)
        self.date_edit = QDateEdit()
        self.date_edit.setObjectName("dateEdit")
        self.date_edit.setStyleSheet("""#dateEdit{
        background-color: rgb(240, 223, 137);
        }""")
        self.date_edit.setDate(self._event.get_date())
        self.horizontalLayout_for_date.addWidget(self.date_edit)
        self.date_edit.setMinimumDate(self.current_date)
        self.date_edit.dateChanged.connect(self.__date_changed)
        self.__fill_in_fields()

    def __date_changed(self):
        self._event.set_date(self.date_edit.date())

    def __check_event_time(self, event_time, curr_hour, curr_minute):
        date_params = [int(i) for i in datetime.now().strftime("%Y %m %d").split()]
        if self._event.get_date() == QDate(*date_params):
            if (event_time.hour() < curr_hour) or (
                    event_time.hour() == curr_hour and event_time.minute() <= curr_minute):
                self.error_message.setText("*значення часу повинно бути більше теперішнього")
                self.dialog.verticalLayout_6.addWidget(self.error_message)
                return False
        return True

    def __check_event_name(self):
        if self.dialog.eventName.text() == "":
            self.error_message.setText("*введіть назву заходу")
            self.dialog.verticalLayout_5.addWidget(self.error_message)
            return False
        return True

    def __check_crossing_with_previous_event(self, event_obj):
        if event_obj != EventContainer.get_events()[0]:
            # if this event is not first, then we get previous event by index current one - 1
            curr_event_ind = EventContainer.get_events().index(event_obj)
            previous_event = EventContainer.get_events()[curr_event_ind - 1]
            previous_event_duration = previous_event.get_duration()[0]
            if previous_event.get_duration()[1] == 0:
                previous_event_duration *= 3600000
            else:
                previous_event_duration *= 60000
            if previous_event_duration >= previous_event.get_date_time().msecsTo(event_obj.get_date_time()):
                self.error_message.setText("Ця подія перетинається з минулою")
                self.dialog.verticalLayout.addWidget(self.error_message)
                return False
        return True

    def __check_crossing_with_next_event(self, event_obj):
        if event_obj != EventContainer.get_events()[-1]:
            # if this event is not last, then we get previous event by index current one + 1
            curr_event_ind = EventContainer.get_events().index(event_obj)
            next_event = EventContainer.get_events()[curr_event_ind + 1]
            event_duration = event_obj.get_duration()[0]
            if event_obj.get_duration()[1] == 0:
                event_duration *= 3600000
            else:
                event_duration *= 60000
            if event_duration >= event_obj.get_date_time().msecsTo(next_event.get_date_time()):
                self.error_message.setText("Ця подія перетинається з наступною")
                self.dialog.verticalLayout.addWidget(self.error_message)
                return False
        return True

    def __delete_event(self):
        EventContainer.remove_reminder(self._event)
        self.accept()

    def __fill_in_fields(self):
        self.dialog.eventName.setText(self._event.get_event_name())
        self.dialog.eventDescription.setPlainText(self._event.get_description())
        self.dialog.hourSpin.setValue(self._event.get_time().hour())
        self.dialog.minuteSpin.setValue(self._event.get_time().minute())
        self.dialog.durationSpin.setValue(self._event.get_duration()[0])
        self.dialog.comboBoxDuration.setCurrentIndex(self._event.get_duration()[1])
        self.dialog.placeEdit.setText(self._event.get_place())

    def _save_event(self):
        if not self.__check_event_name():
            return
        self._event.set_event_name(self.dialog.eventName.text())
        curr_hour, curr_minute = int(datetime.now().strftime("%H")), int(datetime.now().strftime("%M"))
        time_to_write = QTime(self.dialog.hourSpin.value(), self.dialog.minuteSpin.value())
        self._event.set_description(self.dialog.eventDescription.toPlainText())
        if not self.__check_event_time(time_to_write, curr_hour, curr_minute):
            return
        self._event.set_time(time_to_write)
        self._event.set_duration([self.dialog.durationSpin.value(), self.dialog.comboBoxDuration.currentIndex()])
        self._event.set_place(self.dialog.placeEdit.text())
        EventContainer.sort_events()
        if not self.__check_crossing_with_previous_event(self._event):
            return
        self._event.set_date(self.date_edit.date())
        if not self.__check_crossing_with_next_event(self._event):
            return
        EventContainer.add_reminder()
        self.accept()


if __name__ == '__main__':
    try:
        with open(FILE_NAME, "rb") as file:
            while True:
                try:
                    EventContainer.set_data(pickle.load(file))
                except EOFError:
                    break
    except FileNotFoundError:
        with open(FILE_NAME, "x"):
            pass
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    window.check_event()
    app.exec_()
    EventContainer.sort_events()
    with open(FILE_NAME, "wb") as file:
        for event_object in EventContainer.get_events():
            pickle.dump(event_object, file)
    sys.exit()

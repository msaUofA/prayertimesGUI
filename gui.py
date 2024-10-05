import ttkbootstrap as ttk
from dynamic_updater import DynamicUpdater
from prayer_times import read_prayer_times, next_prayer_time

class PrayerTimeGUI(ttk.Window):
    def __init__(self):

        # main window
        super().__init__(themename='darkly')
        self.attributes('-fullscreen', True)
        self.bind('<Escape>', lambda event: self.quit())

        # Frames
        self.main_top_frame = TopFrame(self)
        self.main_bottom_frame = BottomFrame(self)

    def run(self):
        self.mainloop()

class TopFrame(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.place(x=0,y=0, relheight=0.7, relwidth=1)
        self.updater = DynamicUpdater()
        self.create_widget()


    def create_widget(self):

        main_frame = ttk.Frame(self)
        background_label = ttk.Label(main_frame, background='#008028')

        data_frame = ttk.Frame(main_frame)

        clock_frame = ttk.Frame(data_frame)

        title_label = ttk.Label(clock_frame, text='Muslim Student Association',font=('Times New Roman', 45, 'italic'),
                                foreground='#008028', anchor='s')

        live_clock = ttk.Label(clock_frame, font=('Times New Roman', 200, 'bold'), foreground= '#FFE500', anchor = 'center')

        date = ttk.Label(clock_frame, font=('Helvetica', 20, 'bold', 'italic'), anchor='n', foreground='#008028')

        def pack_widgets():

            background_label.place(x=0, y=0, relwidth=1, relheight=1)
            title_label.pack(expand = True, padx =10)
            live_clock.pack(expand=True, fill = 'x',)
            date.pack(expand = True, fill = 'x', padx= 10)
            clock_frame.pack(side = 'left', expand = True, fill = 'both')
            data_frame.pack(expand = True, fill = 'both', padx= 15, pady=15)
            main_frame.pack(expand = True, fill = 'both', padx = 30, pady = 30)



        pack_widgets()
        self.updater.update_clock(live_clock)
        self.updater.update_date(date)

class BottomFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x=0, rely=0.7, relheight=0.3, relwidth=1)
        self.prayer_times = read_prayer_times('prayertimes.csv')
        self.updater = DynamicUpdater()
        self.create_widgets()

    def create_widgets(self):
        def separator(parent):
            ttk.Separator(parent, style='light', orient='vertical').pack(side='left', expand=True, fill='both', pady=35)

        main_frame = ttk.Frame(self)
        background_label = ttk.Label(main_frame, background='#008028')
        prayer_times_frame = ttk.Frame(main_frame)

        fajr = PrayerTimeEntry(prayer_times_frame, 'Fajr', "0")
        separator(prayer_times_frame)

        dhuhr = PrayerTimeEntry(prayer_times_frame, 'Dhuhr',"0")
        separator(prayer_times_frame)

        asr = PrayerTimeEntry(prayer_times_frame, 'Asr', "0")
        separator(prayer_times_frame)

        maghrib = PrayerTimeEntry(prayer_times_frame, 'Maghrib', "0")
        separator(prayer_times_frame)

        isha = PrayerTimeEntry(prayer_times_frame, 'Isha', "0")

        prayer_widgets = {
            'Fajr': fajr,
            'Dhuhr': dhuhr,
            'Asr': asr,
            'Maghrib': maghrib,
            'Isha': isha
        }

        def pack_widgets():

            background_label.place(x=0, y=0, relwidth=1, relheight=1)
            main_frame.pack(expand=True, fill='both', padx=30, pady=30)
            prayer_times_frame.pack(expand=True, fill='both', padx=10, pady=10)

        pack_widgets()
        self.updater.update_prayer_times(self, self.prayer_times, prayer_widgets)

class PrayerTimeEntry(ttk.Frame):
    def __init__(self, parent, prayer_name, prayer_time):
        super().__init__(parent, style='light')
        self.pack(side='left', expand=True, fill='both')

        text_color = '#FFE500'

        self.prayer_name_label = ttk.Label(self, text=prayer_name, font=('Times New Roman', 40, 'bold'), anchor='center', foreground=text_color)
        self.prayer_name_label.pack(expand=True, fill='both')

        self.prayer_time_label = ttk.Label(self, text=prayer_time, font=('Times New Roman', 40), anchor='center', foreground=text_color)
        self.prayer_time_label.pack(expand=True, fill='both')

        if prayer_name == 'Fajr':
            ttk.Label(self, text="Iqamah: 7:00AM", font=('Times New Roman', 13, 'bold'), anchor='center',foreground='grey').pack(expand=True, fill='both')

        if prayer_name == 'Dhuhr':
            ttk.Label(self, text="Iqamah: 2:00PM", font=('Times New Roman', 13, 'bold'), anchor='center', foreground='grey').pack(expand=True, fill='both')

        if prayer_name == 'Asr':
            ttk.Label(self, text="Iqamah: Asr + 10 minutes", font=('Times New Roman', 13, 'bold'), anchor='center', foreground='grey').pack(expand=True, fill='both')

        if prayer_name == 'Maghrib':
            ttk.Label(self, text="Iqamah: Maghrib + 5 minutes", font=('Times New Roman', 13, 'bold'), anchor='center', foreground='grey').pack(expand=True, fill='both')

        if prayer_name == 'Isha':
            ttk.Label(self, text="Iqamah: Isha + 10 minutes", font=('Times New Roman', 13, 'bold'), anchor='center', foreground='grey').pack(expand=True, fill='both')

    def update_time(self, new_prayer_time):
        self.prayer_time_label.config(text=new_prayer_time)


PrayerTimeGUI()



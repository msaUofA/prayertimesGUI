import ttkbootstrap as ttk
import time
import datetime
from datetime import datetime
from hijri_converter import convert
from prayer_times import read_prayer_times

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
        self.prayer_times = read_prayer_times('prayertimes.csv')
        self.clock_widget()


    def clock_widget(self):

        main_frame = ttk.Frame(self, style='success')
        data_frame = ttk.Frame(main_frame)

        clock_frame = ttk.Frame(data_frame)

        # Title label
        label = ttk.Label(clock_frame,
                          text='Muslim Student Association',
                          font=('Times New Roman', 45, 'italic'),
                          style='inverted-success',
                          anchor='s')

        # Live clock
        live_clock = ttk.Label(clock_frame, font=('Times New Roman', 200, 'bold'), style ='success', anchor = 'center')

        # date frame
        next_prayer_frame =  ttk.LabelFrame(data_frame, style = 'success')

        next_prayer_label = ttk.Label(next_prayer_frame, text='Next Prayer is in...',
                                font=('Helvetica', 30, 'bold'),
                                foreground='White',
                                anchor='n')

        next_prayer = ttk.Label(next_prayer_frame)



        date = ttk.Label(clock_frame, font=('Helvetica', 20, 'bold', 'italic'), anchor='n', style = 'success')


        # Pack the live clock with padding
        label.pack(expand = True, padx =10)
        live_clock.pack(expand=True, fill = 'x',)
        date.pack(expand = True, fill = 'x', padx= 10)
        clock_frame.pack(side = 'left', expand = True, fill = 'both')
        data_frame.pack(expand = True, fill = 'both', padx= 30, pady=30)
        # next_prayer_frame.pack(side = 'right' ,expand = True, fill = 'both', padx = 50, pady = 30)
        # next_prayer_label.pack(expand=True, fill='both', padx = 30, pady= 10)
        # next_prayer.pack(expand = True, fill = 'both')
        main_frame.pack(expand = True, fill = 'both', padx = 30, pady = 30)

        def digitalclock():

            current_time = time.strftime("%I:%M%p")

            if current_time[0] == '0':
                current_time = current_time[1:]

            live_clock.config(text=current_time)
            label.after(1000, digitalclock)

        def live_date():

            current_date = datetime.now().strftime("%A, %B %d, %Y")

            hijri_date_obj = convert.Gregorian(datetime.now().year, datetime.now().month, datetime.now().day).to_hijri()
            hijri_date_str = f"{hijri_date_obj.day} {hijri_date_obj.month_name()} {hijri_date_obj.year} AH"

            date.config(text=f'{current_date} - {hijri_date_str}')

            date.after(1000, live_date)


        digitalclock()
        live_date()



class BottomFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x=0, rely=0.7, relheight=0.3, relwidth=1)







PrayerTimeGUI()



import tkinter as tk
import time


def main() -> None:
    """Entry point of clock UI application"""
    # Create window
    window = tk.Tk()
    window.title("Our Clock!")

    # Create label to display clock
    main_clock = tk.Label(
        window, font=("arial", 40, "bold"), background="dark green", foreground="white"
    )

    # Set functionality of clock label
    set_time(clock=main_clock)

    # Pack clock into the main window
    main_clock.pack(anchor="center")

    # Start the Tkinter loop
    tk.mainloop()


def set_time(clock: tk.Label) -> None:
    """
    Sets clock label to display current time.
    Runs once every 1 second.
    """
    current_time = time.strftime("%H:%M:%S %p")
    clock.config(text=current_time)
    clock.after(1000, set_time, clock)


if __name__ == "__main__":
    main()

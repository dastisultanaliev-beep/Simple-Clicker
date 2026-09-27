import tkinter as tk


class Upgrade:
    def __init__(self, name, cost, power, is_auto):
        self.name = name
        self.cost = cost
        self.power = power
        self.is_auto = is_auto
        self.level = 0


class ClickerGame:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Simple Clicker")
        self.root.geometry("800x600")
        self.root.configure(bg="white")

        self.score = 0
        self.click_power = 1
        self.auto_points = 0

        self.upgrades = [
            Upgrade("Stronger Click", 15, 1, False),
            Upgrade("Auto Coins", 30, 1, True)
        ]

        self.create_button()
        self.auto_money()

    def create_button(self):
        self.score_label = tk.Label(
            self.root,
            text="Coins: 0",
            font=("Arial", 22, "bold")
        )
        self.score_label.pack(pady=15)

        self.click_button = tk.Button(
            self.root,
            text="CLICK HERE!!!",
            font=("Arial", 24, "bold"),
            height=3,
            width=20,
            command=self.click
        )
        self.click_button.pack(pady=20)

        tk.Label(
            self.root,
            text="SHOP:",
            font=("Arial", 16, "bold")
        ).pack(pady=5)

        self.shop_buttons = []

        for i, up in enumerate(self.upgrades):
            btn = tk.Button(
                self.root,
                text=f"Buy {up.name} (cost {up.cost})",
                font=("Arial", 24, "bold"),
                command=lambda num=i: self.buy(num)
            )
            btn.pack(pady=8)
            self.shop_buttons.append(btn)

    def click(self):
        self.score = self.score + self.click_power
        self.update_all()

    def buy(self, index):
        up = self.upgrades[index]

        if self.score >= up.cost:
            self.score = self.score - up.cost
            up.level = up.level + 1

            if up.is_auto:
                self.auto_points = self.auto_points + up.power
            else:
                self.click_power = self.click_power + up.power

            up.cost = int(up.cost * 1.7)
            self.update_all()

    def update_all(self):
        self.score_label.config(
            text=f"Coins: {self.score}"
        )

        for i, btn in enumerate(self.shop_buttons):
            up = self.upgrades[i]

            btn.config(
                text=f"Buy {up.name} (cost {up.cost}) "
                     f"Level: {up.level}"
            )

    def auto_money(self):
        self.score = self.score + self.auto_points
        self.update_all()

        self.root.after(1000, self.auto_money)

    def run(self):
        self.root.mainloop()


game = ClickerGame()
game.run()

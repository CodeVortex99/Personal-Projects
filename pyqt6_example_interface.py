from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QVBoxLayout, QComboBox, QTextBrowser, QToolTip
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
import sys

class StockLearningApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("STOMATA - Stock Market Learning Tool")
        self.setGeometry(100, 100, 600, 400)
        self.setStyleSheet("background-color: #111111;")
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        title = QLabel("📈 STOMATA: Learn Trading Visually")
        title.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)

        self.stock_selector = QComboBox()
        self.stock_selector.addItems(["AAPL", "GOOGL", "TSLA"])
        layout.addWidget(self.stock_selector)

        explain = QTextBrowser()
        explain.setHtml("""
        <p><b>Support</b> is a price level where a stock tends to stop falling. 
        <span title='A support level is a price at which buyers tend to enter the market, creating demand and preventing the price from falling further.' style='color:blue; text-decoration: underline; cursor: pointer;'>[?]</span></p>
        <p><b>Resistance</b> is a level where prices tend to stop rising. 
        <span title='A resistance level is a price at which selling pressure tends to emerge, capping further price increases.' style='color:blue; text-decoration: underline; cursor: pointer;'>[?]</span></p>
        """)
        layout.addWidget(explain)

        self.buy_button = QPushButton("Buy")
        self.sell_button = QPushButton("Sell")
        self.observe_button = QPushButton("Observe")
        for btn in [self.buy_button, self.sell_button, self.observe_button]:
            btn.setStyleSheet("padding: 10px; font-size: 14px;")
            layout.addWidget(btn)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StockLearningApp()
    window.show()
    sys.exit(app.exec())

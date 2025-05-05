# Café Management System

## Overview
The Café Management System is a Python-based application designed to streamline the management of café operations. It allows users to display a menu, take orders, view current orders, generate bills, and exit the system. The application is structured to facilitate easy updates and maintenance.

## Features
- **Menu Management**: Load, display, and update menu items from a JSON file.
- **Order Management**: Take and view orders, with the ability to manage the order list.
- **Billing**: Generate bills with accurate totals and clear orders after billing.
- **Persistent Storage**: Store menu items and orders in JSON format for easy updates and persistent data between application runs.
- **Unit Testing**: Comprehensive tests for menu, order, and billing functionalities to ensure reliability.

## Project Structure
```
cafe-management-system
├── src
│   ├── main.py          # Entry point of the application
│   ├── menu.py          # Menu management functionalities
│   ├── orders.py        # Order management functionalities
│   ├── billing.py       # Billing functionalities
│   └── utils
│       └── helpers.py   # Utility functions
├── data
│   ├── menu.json        # Menu items in JSON format
│   └── orders.json      # Orders in JSON format
├── tests
│   ├── test_menu.py     # Unit tests for menu functionalities
│   ├── test_orders.py    # Unit tests for order management
│   └── test_billing.py   # Unit tests for billing functionalities
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   cd cafe-management-system
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python src/main.py
   ```

## Usage Guidelines
- Start the application and follow the on-screen prompts to navigate through the menu.
- Use the options to display the menu, take orders, view current orders, and generate bills.
- The menu and orders are stored in JSON files, which can be modified directly for updates.

## Contribution
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License.
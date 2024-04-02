import pytest
from tkinter import messagebox
from source.copilot_test import button_equal


def test_button_equal_valid_expression(mocker):
    # Mocking the entry and tk.END
    entry_mock = mocker.Mock()
    entry_mock.get.return_value = "2 + 2"
    entry_mock.delete.return_value = None
    entry_mock.insert.return_value = None

    # Mocking the eval function
    eval_mock = mocker.patch("__main__.eval")
    eval_mock.return_value = 4

    # Mocking the messagebox.showerror function
    messagebox_mock = mocker.patch("tkinter.messagebox.showerror")

    # Calling the button_equal function
    button_equal()

    # Assertions
    entry_mock.get.assert_called_once()
    entry_mock.delete.assert_called_once_with(0, mocker.ANY)
    entry_mock.insert.assert_called_once_with(mocker.ANY, 4)
    eval_mock.assert_called_once_with("2 + 2")
    messagebox_mock.assert_not_called()


def test_button_equal_invalid_expression(mocker):
    # Mocking the entry and tk.END
    entry_mock = mocker.Mock()
    entry_mock.get.return_value = "2 / 0"
    entry_mock.delete.return_value = None
    entry_mock.insert.return_value = None

    # Mocking the eval function
    eval_mock = mocker.patch("__main__.eval")
    eval_mock.side_effect = ZeroDivisionError("division by zero")

    # Mocking the messagebox.showerror function
    messagebox_mock = mocker.patch("tkinter.messagebox.showerror")

    # Calling the button_equal function
    button_equal()

    # Assertions
    entry_mock.get.assert_called_once()
    entry_mock.delete.assert_called_once_with(0, mocker.ANY)
    entry_mock.insert.assert_not_called()
    eval_mock.assert_called_once_with("2 / 0")
    messagebox_mock.assert_called_once_with("Error", "division by zero")

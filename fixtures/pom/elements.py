import pytest

from core.web.entities.browser_page import BrowserPage
from pom.elements.dialog_element import DialogElement
from pom.elements.editor_dialog_element import EditorDialogElement
from pom.elements.navigation_element import NavigationElement


@pytest.fixture()
def nav_element() -> NavigationElement | BrowserPage:
    return NavigationElement()


@pytest.fixture()
def dialog_element() -> DialogElement:
    return DialogElement()


@pytest.fixture()
def editor_dialog_element() -> EditorDialogElement:
    return EditorDialogElement()

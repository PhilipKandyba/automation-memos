from core import faker
from entities.user import User
from pom.pages.main_page import MainPage
from pom.elements.dialog_element import DialogElement
from pom.elements.editor_dialog_element import EditorDialogElement


def test_create_memo(logged_user: User, main_page: MainPage):
    """
    CaseId: 3
    """
    memo_text = faker.text()

    main_page.page.open()
    main_page.EDITOR_INPUTER.fill(text=memo_text)
    main_page.EDITOR_SUBMIT_BUTTON.click()
    assert main_page.LATEST_MEMO_ITEM.is_present()
    assert main_page.LATEST_MEMO_ITEM_CONTENT.has_text(expected_text=memo_text)


def test_delete_memo(
    logged_user: User, main_page: MainPage, dialog_element: DialogElement
):
    """
    CaseId: 4
    """
    memo_text = faker.text()

    logged_user.memos.create_memo(content=memo_text)
    main_page.page.open()
    main_page.LATEST_MEMO_ITEM_SUBMENU.click()
    main_page.MEMO_ITEM_SUBMENU_DELETE_BUTTON.click()
    dialog_element.CONFIRM_BUTTON.click()

    assert main_page.LATEST_MEMO_ITEM_CONTENT.is_not_present()


def test_update_memo(
    logged_user: User,
    main_page: MainPage,
    editor_dialog_element: EditorDialogElement,
):
    """
    CaseId: 5
    """
    memo_text = faker.text()

    logged_user.memos.create_memo(content=memo_text)
    main_page.page.open()
    main_page.LATEST_MEMO_ITEM_SUBMENU.click()
    main_page.MEMO_ITEM_SUBMENU_EDIT_BUTTON.click()

    updated_memo_text = faker.text()
    editor_dialog_element.EDITOR_INPUTER.fill(text=updated_memo_text)
    editor_dialog_element.EDITOR_SUBMIT_BUTTON.click()

    assert main_page.LATEST_MEMO_ITEM_CONTENT.has_text(
        expected_text=updated_memo_text + "make test fail"
    )

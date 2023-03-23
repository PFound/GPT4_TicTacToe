import pytest
import pygame
from button import Button

@pytest.fixture
def button():
    pygame.init()
    font = pygame.font.Font(None, 36)
    return Button(50, 50, 200, 40, "Test Button", font, (255, 255, 255), (0, 0, 0))

def test_button_initialization(button):
    assert button.rect.x == 50
    assert button.rect.y == 50
    assert button.rect.width == 200
    assert button.rect.height == 40

def test_button_is_clicked(button):
    assert button.is_clicked((55, 55)) == True
    assert button.is_clicked((100, 80)) == True  # Use a point inside the button's boundaries
    assert button.is_clicked((249, 89)) == True
    assert button.is_clicked((250, 90)) == False

#include <iostream>
#include <cstdlib>
#include <SFML/Graphics.hpp>
#include "utils.h"

using namespace sf;

std::string get_resource_path(
	const char* game,
	const char* resource_type)

int main(int argc, char** argv) {

	//need to check available videomodes
	for (unsigned int i= 0; i < sf::VideoMode::GetModesCount(); ++i) {
		sf::VideoMode mode = sf::VideoMode::GetMode(i);
		std::cout << "Mode "
				  << Mode.Width << "-"
				  << Mode.Height << "-"
				  << Mode.BitsPerPixel
				  << " is valid"
				  << std::endl;
	}


	VideoMode
		video_mode(1920, 1080);
	RenderWindow
		window(
			video_mode,
			"Timber!!!",
			Style::Fullscreen);
	Texture
		texture_background;
	texture_background
		.loadFromFile(
			get_resource(
				"zombies",
				Resource::graphics,
				"background.png"));
	Sprite
		sprite_background;
	sprite_background
		.setTexture(
			texture_background:w
		)
		.setPosition(
			0, 0)

	while (window.isOpen()){
		if (Keyboard::isKeyPressed(Keyboard::Escape)){
			window.close()
		}

		window.clear();

		window.draw(
			sprite_background);

		window.display();
	}
}


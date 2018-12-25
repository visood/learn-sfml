#include <iostream>
#include <cstdlib>
#include <SFML/Graphics.hpp>
#include "utils.h"

using namespace sf;

int main(int argc, char** argv) {

    for (const auto& mode: VideoMode::getFullscreenModes()) {
		std::cout << "Mode "
				  << mode.width << "-"
				  << mode.height << "-"
				  << mode.bitsPerPixel
				  << " is valid"
				  << std::endl;
	}
	VideoMode
       video_mode(2048, 1536, 32);
    std::cout << "Selected video mode "
              << video_mode.width << " X "
              << video_mode.height << " X "
              << video_mode.bitsPerPixel
              << (video_mode.isValid() ? " is " : " is not ") << " valid."
              << std::endl;
	RenderWindow
		window(
			video_mode,
			"Timber!!!",
			Style::Fullscreen);
    std::cout << "rendered window"
              << std::endl;
	Texture
		texture_background;
	texture_background
		.loadFromFile(
			get_resource(
				"timber",
				Resource::graphics,
				"background.png"));
    std::cout << "textured background"
              << std::endl;
	Sprite
		sprite_background;
	sprite_background.setTexture(
		texture_background);
	sprite_background.setPosition(
		0, 0);
	while (window.isOpen()){
		sf::Event event;
		while (window.pollEvent(event)) {
			if (event.type == sf::Event::Closed)
				window.close();
		}
		window.clear();
		window.draw(
            sprite_background);
		window.display();
	}
}


#include <iostream>
#include <cstdlib>
#include "utils.h"

namespace fs = std::filesystem;

fs::path get_resource_path(
	const std::string& game,
	const Resource& resource_type)
{
	const fs::path resources=
		std::getenv(
			"RESOURCES");
	switch (resource_type) {
	case Resource::graphics :
		return resources / game / "graphics";
	case Resource::sounds :
		return resources / game / "sounds";
	case Resource::fonts :
		return resources / game / "fonts";
	}
	return resources; //or throw an exception
}
fs::path get_resource(
	const std::string& game,
	const Resource& resource_type,
	const char* resource_name)
{
	const fs::path resource_path=
		get_resource_path(game, resource_type);
	return resource_path / resource_name;
}


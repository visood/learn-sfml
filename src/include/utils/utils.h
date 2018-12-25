/*
  utilities
 */

#include <filesystem>

enum class Resource
{
	graphics,
	sounds,
	fonts
};

std::filesystem::path get_resource_path(
	const std::string& game,
	const Resource& resource_type);

std::filesystem::path get_resource(
	const std::string& game,
	const Resource& resource_type,
	const char* resource_name);


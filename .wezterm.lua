-- Pull in the wezterm API
local wezterm = require("wezterm")

-- This will hold the configuration.
local config = wezterm.config_builder()

-- This is where you actually apply your config choices

-- For example, changing the color scheme:
-- config.color_scheme = 'Bamboo'
-- config.color_scheme = "PhD (base16)"
config.color_scheme = "Material Darker (base16)"

config.hide_tab_bar_if_only_one_tab = true
config.font = wezterm.font("Monofur Nerd Font")
config.font_size = 18
config.window_padding = {
	left = 0,
	right = 0,
	top = 0,
	bottom = 0,
}

wezterm.on("gui-startup", function()
	local tab, pane, window = wezterm.mux.spawn_window({})
	window:gui_window():maximize()
end)

local act = wezterm.action

config.keys = {
	{ key = "PageUp", mods = "SHIFT", action = act.ScrollByPage(-1) },
	{ key = "PageDown", mods = "SHIFT", action = act.ScrollByPage(1) },
}

-- and finally, return the configuration to wezterm
return config

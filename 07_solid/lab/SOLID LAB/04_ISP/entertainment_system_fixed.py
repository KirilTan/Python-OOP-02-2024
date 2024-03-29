class HDMI:
    def connect_to_device_via_hdmi_cable(self, device):
        ...


class RCA:
    def connect_to_device_via_rca_cable(self, device):
        ...


class PowerOutlet:
    def connect_device_to_power_outlet(self, device):
        ...


class Ethernet:
    def connect_to_device_via_ethernet_cable(self, device):
        ...


class TV(RCA, HDMI, PowerOutlet):
    def connect_to_tv(self, television):
        super().connect_to_device_via_rca_cable(television)

    def connect_to_game_console(self, game_console):
        super().connect_to_device_via_hdmi_cable(game_console)

    def plug_in_power(self):
        super().connect_device_to_power_outlet(self)


class DVDPlayer(HDMI, PowerOutlet):
    def connect_to_tv(self, television):
        super().connect_to_device_via_hdmi_cable(television)

    def plug_in_power(self):
        super().connect_device_to_power_outlet(self)


class GameConsole(HDMI, Ethernet, PowerOutlet):
    def connect_to_tv(self, television):
        super().connect_to_device_via_hdmi_cable(television)

    def connect_to_router(self, router):
        super().connect_to_device_via_ethernet_cable(router)

    def plug_in_power(self):
        super().connect_device_to_power_outlet(self)


class Router(Ethernet, PowerOutlet):
    def connect_to_tv(self, television):
        super().connect_to_device_via_ethernet_cable(television)

    def connect_to_game_console(self, game_console):
        super().connect_to_device_via_ethernet_cable(game_console)

    def plug_in_power(self):
        super().connect_device_to_power_outlet(self)

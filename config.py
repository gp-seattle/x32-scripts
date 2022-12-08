config = {
    "personal": {
        "DPA": {
            "channels": ["01"]
        },
        "HH1": {
            "channels": ["02"]
        },
        "HH2": {
            "channels": ["03"]
        },
        "Vocals 1": {
            "channels": ["05", "09"],
            "iem_bus": "01"
        },
        "Vocals 2": {
            "channels": ["06"],
            "iem_bus": "03"
        },
        "Vocals 3": {
            "channels": ["07"],
            "iem_bus": "05"
        },
        "Keys": {
            "channels": ["10", "11", "12"],
            "iem_bus": "09"
        },
        "EG": {
            "channels": ["13"],
            "iem_bus": "11"
        },
        "Bass": {
            "channels": ["15", "16"],
            "iem_bus": "13"
        },
        "Drums": {
            "iem_bus": "15"
        }
    },
    "settings": {
        "Vocal FX": ["/fxrtn/01/mix/fader", "/fxrtn/01/mix/on", "/fxrtn/03/mix/fader", "/fxrtn/03/mix/on"],
        "Instru Mutes": [
            "/ch/05/mix/on", "/ch/06/mix/on", "/ch/07/mix/on", "/ch/08/mix/on",
            "/ch/09/mix/on", "/ch/10/mix/on", "/ch/11/mix/on", "/ch/12/mix/on",
            "/ch/13/mix/on", "/ch/14/mix/on", "/ch/15/mix/on", "/ch/16/mix/on",
            "/ch/17/mix/on", "/ch/18/mix/on", "/ch/19/mix/on", "/ch/20/mix/on",
            "/ch/21/mix/on", "/ch/22/mix/on",
            "/ch/26/mix/on", "/ch/27/mix/on", "/ch/28/mix/on",
            "/dca/1/on", "/dca/2/on", "/dca/3/on", "/dca/4/on", "/dca/5/on"
        ]
    },
    "osc": {
        "foh": "10.246.1.10",
        "iem": "10.246.1.15"
    },
    "serverMidi": "X-USB",
    "midi": {
        "audio": "X32Helper",
        "video": "Network Session 1",
        "light": "Gracepoint‚Äôs Mac mini Bluetooth"
    },
    "faders": {
        "VOX EQ": {"commands": ["foh /ch/05/eq/1/g 0.4 0.5"]},
        "VOX Pan": {"commands": ["foh /ch/06/mix/pan 0.5 0.2", "foh /ch/07/mix/pan 0.5 0.8"]},
        "EG/Keys Pan": {"commands": ["foh /ch/13/mix/pan 0.5 0.2", "foh /ch/11/mix/pan 0.5 0.8"]},
        "Bass/Drums HPF": {"commands": ["foh /ch/15/mix/pan 0.3 0.0", "foh /ch/18/mix/pan 0.3 0.0", "foh /ch/20/mix/pan 0.3 0.0"]},
        "VOX Tracks": {"defaultValue": 63, "commands": ["midi audio 2 50"]},
        "EG/Keys Tracks": {"defaultValue": 63, "commands": ["midi audio 2 51"]},
        "Bass Tracks": {"defaultValue": 63, "commands": ["midi audio 2 52"]},
        "Drum Tracks": {"defaultValue": 63, "commands": ["midi audio 2 53"]},
    }
}
import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import climate, climate_ir, remote_transmitter, remote_receiver
from esphome.const import CONF_ID

AUTO_LOAD = ["climate_ir"]

mirage_ns = cg.esphome_ns.namespace("mirage")
MirageClimate = mirage_ns.class_("MirageClimate", climate_ir.ClimateIR)

# --- THE 2025 COMPATIBLE FIX ---
# We use the new 'climate_schema' function instead of the old constants
CONFIG_SCHEMA = climate.climate_schema(MirageClimate).extend(
    {
        cv.GenerateID(): cv.declare_id(MirageClimate),
        cv.Optional("transmitter_id"): cv.use_id(remote_transmitter.RemoteTransmitterComponent),
        cv.Optional("receiver_id"): cv.use_id(remote_receiver.RemoteReceiverComponent),
    }
)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await climate_ir.register_climate_ir(var, config)

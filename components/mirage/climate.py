import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import climate_ir, remote_receiver, sensor
from esphome.const import CONF_ID, CONF_SENSOR, CONF_RECEIVER_ID

# Dependencies - climate_ir handles climate registration
AUTO_LOAD = ["climate_ir"]
CODEOWNERS = ["@stefangordon"]

mirage_ns = cg.esphome_ns.namespace("mirage")
MirageClimate = mirage_ns.class_("MirageClimate", climate_ir.ClimateIR)

# Use the standard climate_ir schema which already includes transmitter_id
# and properly registers with Home Assistant
CONFIG_SCHEMA = climate_ir.CLIMATE_IR_WITH_RECEIVER_SCHEMA.extend(
    {
        cv.GenerateID(): cv.declare_id(MirageClimate),
    }
)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    
    # This is the key function - it:
    # 1. Registers the component
    # 2. Registers the climate entity (makes it show in HA/web UI)
    # 3. Sets up the transmitter
    # 4. Sets up supports_cool/heat from config
    # 5. Sets up sensor if provided
    await climate_ir.register_climate_ir(var, config)
    
    # Set up the receiver if provided
    if CONF_RECEIVER_ID in config:
        receiver = await cg.get_variable(config[CONF_RECEIVER_ID])
        cg.add(receiver.register_listener(var))

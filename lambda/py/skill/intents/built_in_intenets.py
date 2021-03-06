"""
Filename: built_in_intents.py

Description: takes care of all the amazon built-in intents
"""
#--------------------------------------------------------------------------
# AwS Libraries
#--------------------------------------------------------------------------
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_core.dispatch_components import (
    AbstractRequestHandler, AbstractExceptionHandler,
    AbstractResponseInterceptor, AbstractRequestInterceptor)
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_model.ui import SimpleCard
from ask_sdk_model import Response

#--------------------------------------------------------------------------
# Python Libraries
#--------------------------------------------------------------------------
import logging
import gettext

#--------------------------------------------------------------------------
# Resource Libraries
#--------------------------------------------------------------------------
from skill.resources import data, util

# Set Logging 
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In HelpIntentHandler")
        _ = handler_input.attributes_manager.request_attributes["_"]

        item = util.get_random_item()

        speech = _(data.HELP_MESSAGE).format(item)

        handler_input.response_builder.speak(speech).ask(speech)
        return handler_input.response_builder.response

class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Handler for Cancel and Stop Intents."""
    def can_handle(self, handler_input):
        return (is_intent_name("AMAZON.CancelIntent")(handler_input) or
                is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In CancelOrStopIntentHandler")
        _ = handler_input.attributes_manager.request_attributes["_"]

        speech = _(data.STOP_MESSAGE).format(_(data.SKILL_NAME))
        handler_input.response_builder.speak(speech)

        return handler_input.response_builder.response

class RepeatIntentHandler(AbstractRequestHandler):
    """Handler for Repeat Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.RepeatIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In RepeatIntentHandler")
        _ = handler_input.attributes_manager.request_attributes["_"]

        attr = handler_input.attributes_manager.session_attributes
        handler_input.response_builder.speak(
            attr['speech']).ask(
            attr['reprompt'])
        return handler_input.response_builder.response

class FallbackIntentHandler(AbstractRequestHandler):
    """Handler for Fallback Intent.

    Used for catching instances that aren't covered by the skill
    """
    def can_handle(self, handler_input):
        return is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In FallbackIntentHandler")
        _ = handler_input.attributes_manager.request_attributes["_"]

        # Nab a random item for an example
        item = util.get_random_item()

        help_message = _(data.HELP_MESSAGE).format(item)
        help_reprompt = _(data.HELP_REPROMPT).format(item)

        # Format the speech output
        speech = _(data.FALLBACK_MESSAGE).format(
            _(data.SKILL_NAME)) + help_message
        reprompt = _(data.FALLBACK_MESSAGE).format(
            _(data.SKILL_NAME)) + help_reprompt

        handler_input.response_builder.speak(speech).ask(reprompt)
        return handler_input.response_builder.response

class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for SessionEndedRequest."""
    def can_handle(self, handler_input):
        return is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In SessionEndedRequestHandler")
        logger.info("Session ended with reason: {}".format(
            handler_input.request_envelope.request.reason))
        return handler_input.response_builder.response

class YesIntentHandler(AbstractRequestHandler):
    """Handler for the YesIntent."""
    def can_handle(self, handler_input):
        return is_intent_name("AMAZON.YesIntent")(handler_input)

    def handle(self, handler_input):
        logger.debug("In YesIntentHandler")
        _ = handler_input.attributes_manager.request_attributes["_"]
        session_attr = handler_input.attributes_manager.session_attributes

        #Get what the previous intent was
        prev_intent = session_attr.get("PREV_INTENT")

        if prev_intent == "LaunchIntent":
            speech = data.HELP_MESSAGE
            reprompt = data.FALLBACK_MESSAGE

            handler_input.response_builder.speak(speech) \
            .set_should_end_session(False).ask(reprompt)
            return handler_input.response_builder.response

        if (prev_intent == "RecipeIntent"
            or prev_intent == "RandomItemIntent"
            or prev_intent == "AMAZON.YesIntent"
            or prev_intent == "AMAZON.NoIntent"):
            speech = data.HELP_MESSAGE
            reprompt = data.FALLBACK_MESSAGE

            handler_input.response_builder.speak(speech) \
            .set_should_end_session(False).ask(reprompt)
            return handler_input.response_builder.response


class NoIntentHandler(AbstractRequestHandler):
    """Handler for the NoIntent. Sometimes its okay to say no"""
    def can_handle(self, handler_input):
        return is_intent_name("AMAZON.NoIntent")(handler_input)

    def handle(self, handler_input):
        logger.debug("In NoIntentHandler")
        _ = handler_input.attributes_manager.request_attributes["_"]
        
        speech = data.STOP_MESSAGE
        handler_input.response_builder.speak(_(speech))
            .set_should_end_session(True)

        return handler_input.response_builder.response


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Global exception handler."""
    def can_handle(self, handler_input, exception):
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        _ = handler_input.attributes_manager.request_attributes["_"]
        logger.error(exception, exc_info=True)
        logger.info("Original request was {}".format(
            handler_input.request_envelope.request))

        speech = _("Sorry, I can't understand the command. Please say again!")
        handler_input.response_builder.speak(speech).ask(speech)

        return handler_input.response_builder.response

class CacheSpeechForRepeatInterceptor(AbstractResponseInterceptor):
    """Cache the output speech and reprompt to session attributes,
    for repeat intent.
    """
    def process(self, handler_input, response):
        # type: (HandlerInput, Response) -> None
        session_attr = handler_input.attributes_manager.session_attributes
        session_attr["speech"] = response.output_speech
        session_attr["reprompt"] = response.reprompt


class LocalizationInterceptor(AbstractRequestInterceptor):
    """Add function to request attributes, that can load locale specific data."""
    def process(self, handler_input):
        # type: (HandlerInput) -> None
        locale = handler_input.request_envelope.request.locale
        logger.info("Locale is {}".format(locale))
        i18n = gettext.translation(
            'data', localedir='locales', languages=[locale], fallback=True)
        handler_input.attributes_manager.request_attributes["_"] = i18n.gettext


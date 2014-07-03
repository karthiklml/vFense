import logging

from json import dumps

from vFense import VFENSE_LOGGING_CONFIG
from vFense.core.api.base import BaseHandler
from vFense.core.decorators import agent_authenticated_request, \
    convert_json_to_arguments
from vFense.core.user.manager import UserManager
from vFense.core.user import UserKeys

from vFense.result.error_messages import GenericResults, \
    UpdateApplicationsResults

from vFense.receiver.rvhandler import RvHandOff

from vFense.core.operations._constants import AgentOperations

logging.config.fileConfig(VFENSE_LOGGING_CONFIG)
logger = logging.getLogger('rvlistener')


class AgentUpdateHandler(BaseHandler):
    @agent_authenticated_request
    @convert_json_to_arguments
    def put(self, agent_id):
        username = self.get_current_user()
        view_name = (
            UserManager(username).get_attribute(UserKeys.CurrentView)
        )

        uri = self.request.uri
        method = self.request.method

        try:
            operation_id = self.arguments.get('operation_id', None)
            error = self.arguments.get('error', None)
            success = self.arguments.get('success', 'true')
            app_data = self.arguments.get('data')
            status_code = self.arguments.get('status_code', None)

            RvHandOff(
            ).available_agent_update_operation(agent_id, app_data)

            results = (
                UpdateApplicationsResults(username, uri, method)
                .applications_updated(agent_id, app_data)
            )

            results['data'] = []
            self.set_status(results['http_status'])
            self.write(dumps(results))

        except Exception as e:
            results = GenericResults(
                username, uri, method
            ).something_broke(
                agent_id, AgentOperations.AVAILABLE_AGENT_UPDATE, e
            )
            logger.exception(results)

            self.set_status(results['http_status'])
            self.write(dumps(results))

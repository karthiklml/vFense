import unittest
from json import dumps

from vFense.core.agent._db_model import (
    AgentKeys
)
from vFense.core.tag import Tag
from vFense.core.tag._db_model import TagKeys
from vFense.core.tag._db import fetch_tag_by_name_and_view
from vFense.core.agent._db import fetch_agent_ids_in_view
from vFense.core.tag.manager import TagManager
from vFense.core.agent import Agent
from vFense.core.agent.manager import AgentManager
from vFense.errorz.status_codes import (
    AgentCodes, AgentResultCodes, TagCodes, ViewCodes
)
from vFense.errorz._constants import ApiResultKeys
from vFense.core.agent._constants import AgentDefaults
from vFense.core.tests.agent_and_tag_data import AGENT_DATA
from vFense.core.view._constants import DefaultViews
from vFense.core.view import View
from vFense.core.view.manager import ViewManager

class AgentsAndTagsTests(unittest.TestCase):

    def test_a_create_view1(self):
        view = View(
            'Test View 1',
        )
        manager = ViewManager(view.name)
        results = manager.create(view)
        print dumps(results, indent=4)
        status_code = results.get(ApiResultKeys.VFENSE_STATUS_CODE)
        self.failUnless(status_code == ViewCodes.ViewCreated)

    def test_a_create_view2(self):
        view = View(
            'Test View 2',
        )
        manager = ViewManager(view.name)
        results = manager.create(view)
        print dumps(results, indent=4)
        status_code = results.get(ApiResultKeys.VFENSE_STATUS_CODE)
        self.failUnless(status_code == ViewCodes.ViewCreated)

    def test_b_create_tag1(self):
        tag = (
            Tag(
                'Global Test Tag 1', view_name=DefaultViews.GLOBAL,
                is_global=True
            )
        )
        manager = TagManager()
        results = manager.create(tag)
        print dumps(results, indent=4)
        status_code = results.get(ApiResultKeys.VFENSE_STATUS_CODE)
        self.failUnless(status_code == TagCodes.TagCreated)

    def test_b_create_tag2(self):
        tag = Tag('Local Test Tag 1', view_name='Test View 2')
        manager = TagManager()
        results = manager.create(tag)
        print dumps(results, indent=4)
        status_code = results.get(ApiResultKeys.VFENSE_STATUS_CODE)
        self.failUnless(status_code == TagCodes.TagCreated)

    def test_c_create_agent1(self):
        system_info = AGENT_DATA["system_info"]
        system_info[AgentKeys.Views] = AGENT_DATA[AgentKeys.Views]
        system_info[AgentKeys.Hardware] = AGENT_DATA[AgentKeys.Hardware]
        agent = Agent(**system_info)
        tag = (
            fetch_tag_by_name_and_view(
                'Global Test Tag 1', DefaultViews.GLOBAL
            )
        )
        manager = AgentManager()
        results = manager.create(agent, tags=[tag[TagKeys.TagId]])
        print dumps(results, indent=4)
        status_code = results.get(ApiResultKeys.VFENSE_STATUS_CODE)
        self.failUnless(status_code == AgentResultCodes.NewAgentSucceeded)

    def test_d_tag_add_to_agent(self):
        tag = (
            fetch_tag_by_name_and_view(
                'Local Test Tag 1', 'Test View 2'
            )
        )
        agent_ids = fetch_agent_ids_in_view()
        manager = TagManager(tag[TagKeys.TagId])
        results = manager.add_agents(agent_ids)
        print dumps(results, indent=4)
        status_code = results.get(ApiResultKeys.VFENSE_STATUS_CODE)
        self.failUnless(status_code == TagCodes.AgentsAddedToTag)

    def test_e_tag_remove_from_agent(self):
        tag = (
            fetch_tag_by_name_and_view(
                'Local Test Tag 1', 'Test View 2'
            )
        )
        agent_ids = fetch_agent_ids_in_view()
        manager = TagManager(tag[TagKeys.TagId])
        results = manager.remove_agents(agent_ids)
        print dumps(results, indent=4)
        status_code = results.get(ApiResultKeys.VFENSE_STATUS_CODE)
        self.failUnless(status_code == TagCodes.AgentsRemovedFromTag)


def main():
    unittest.main()

if __name__ == '__main__':
    main()
import dotenv
from crewai import Agent, Crew, Task
from crewai.project import CrewBase, agent, crew, task

from tools import count_letters

dotenv.load_dotenv()


@CrewBase
class TranslatorCrew:
    @agent
    def translator_agent(self) -> Agent:
        return Agent(config=self.agents_config["translator_agent"])

    @agent
    def counter_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["counter_agent"],
            tools=[count_letters],
        )

    @task
    def translate_task(self) -> Task:
        return Task(config=self.tasks_config["translate_task"])

    @task
    def retranslate_task(self) -> Task:
        return Task(config=self.tasks_config["retranslate_task"])

    @task
    def count_task(self) -> Task:
        return Task(config=self.tasks_config["count_task"])

    @crew
    def assemble_crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            verbose=True,
        )


TranslatorCrew().assemble_crew().kickoff(
    inputs={
        "sentence": "I'm a software engineer, my name is Jinwook",
    }
)

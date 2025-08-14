import dotenv
from crewai import Agent, Crew, Task
from crewai.project import CrewBase, agent, crew, task

dotenv.load_dotenv()


@CrewBase
class TranslatorCrew:
    @agent
    def translator_agent(self) -> Agent:
        return Agent(config=self.agents_config["translator_agent"])

    @task
    def translate_task(self) -> Task:
        return Task(config=self.tasks_config["translate_task"])

    @task
    def retranslate_task(self) -> Task:
        return Task(config=self.tasks_config["retranslate_task"])

    @crew
    def assemble_crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            verbose=True,
        )


TranslatorCrew().assemble_crew().kickoff(
    inputs={
        "article": "The news article is about the latest technology trends in the world.",
    }
)

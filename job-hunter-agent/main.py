import dotenv


from crewai import Agent, Crew, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.knowledge.source.text_file_knowledge_source import TextFileKnowledgeSource
from models import JobList, RankedJobList, ChosenJob
from tools import web_search_tool


dotenv.load_dotenv()

knowledge_source = TextFileKnowledgeSource(file_path=["resume.txt"])


@CrewBase
class JobHunterCrew:
    #################### AGENTS ####################
    @agent
    def job_search_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["job_search_agent"],
            tools=[web_search_tool],
        )

    @agent
    def job_matching_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["job_matching_agent"],
            knowledge_sources=[knowledge_source],
        )

    @agent
    def resume_optimization_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["resume_optimization_agent"],
            knowledge_sources=[knowledge_source],
        )

    @agent
    def company_research_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["company_research_agent"],
            knowledge_sources=[knowledge_source],
            tools=[web_search_tool],
        )

    @agent
    def interview_prep_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["interview_prep_agent"],
            knowledge_sources=[knowledge_source],
        )

    #################### TASKS ####################
    @task
    def job_extraction_task(self) -> Task:
        return Task(
            config=self.tasks_config["job_extraction_task"],
            output_pydantic=JobList,
        )

    @task
    def job_matching_task(self) -> Task:
        return Task(
            config=self.tasks_config["job_matching_task"],
            output_pydantic=RankedJobList,
        )

    @task
    def job_selection_task(self) -> Task:
        return Task(
            config=self.tasks_config["job_selection_task"],
            output_pydantic=ChosenJob,
        )

    @task
    def resume_rewriting_task(self) -> Task:
        return Task(
            config=self.tasks_config["resume_rewriting_task"],
            context=[
                # 이전 task에서 이어지기 떄문에 생략 가능
                self.job_selection_task(),
            ],
        )

    @task
    def company_research_task(self) -> Task:
        return Task(
            config=self.tasks_config["company_research_task"],
            context=[
                self.job_selection_task(),
            ],
        )

    @task
    def interview_prep_task(self) -> Task:
        return Task(
            config=self.tasks_config["interview_prep_task"],
            context=[
                self.job_selection_task(),
                self.resume_rewriting_task(),
                self.company_research_task(),
            ],
        )

    #################### CREW ####################
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            verbose=True,
        )


result = (
    JobHunterCrew()
    .crew()
    .kickoff(
        inputs={
            "level": "Senior",
            "position": "Golang Developer",
            "location": "Germany",
        }
    )
)

for task_output in result.tasks_output:
    print(task_output.pydantic)

import os
from dotenv import load_dotenv
from SpeechAce import SpeechAce


load_dotenv()
api_key = os.getenv("SPEECHACE_API_KEY")
speechace = SpeechAce(api_key)

task_type = "describe-image"
task_context = "Question: You are a senior college student. Liu Hong is a new student in your department. You are aware \
that Liu Hong has been under a lot of stress with study and is on treatment for depression. This \
morning Liu Hong asked you to have a read at one of her final essays and offer her some feedback. \
You read the essay and noticed it was badly written, with chunks of paragraphs plagiarised from \
other sources. Liu Hong told you she had to submit this paper tomorrow morning. You decide to \
send her a voice message to talk about her essay. \
Rubrics: \
1 - contains inappropriate phrasing and an inconsistent tone, leading to confusion and a lack of clarity. \
3 - generally uses appropriate phrasing and tone, but there are occasional lapses or unclear expressions. \
5 - consistently demonstrates excellent phrasing and tone, conveying the intended meaning clearly and effectively, with a professional and respectful approach."

task_context = "Rubrics: \
0 - lacks logical structure and the meaning cannot be understood. \
1 - has a disorganized structure, unclear expression, and fails to convey information accurately. \
2 - has some logical structure issues but can be somewhat understood. \
3 - has a generally clear logical structure and is able to convey information, but there are some inaccuracies or vague expressions. \
4 - has a clear logical structure, accurately conveys information, but may have minor expression issues. \
5 - has a highly clear logical structure, precise and clear expression, and can fully convey information."

task_context = "Rubrics: \
0 - is filled with inappropriate and offensive language, making it disrespectful and impossible to comprehend. \
1 - contains inappropriate phrasing and an inconsistent tone, leading to confusion and a lack of clarity. \
2 - has some phrasing issues and an inconsistent tone, making it somewhat difficult to understand the intended meaning. \
3 - generally uses appropriate phrasing and tone, but there are occasional lapses or unclear expressions. \
4 - consistently uses appropriate phrasing and tone, effectively conveying the intended meaning, with only minor areas for improvement. \
5 - consistently demonstrates excellent phrasing and tone, conveying the intended meaning clearly and effectively, with a professional and respectful approach."


task_context = "Answer should contain the following key points: \
(1) Feedback on the final essay, mentioning that I have identified plagiarized chunks. \
(2) Emphasizing the severity of plagiarism and discouraging Liu Hong from submitting an essay with suspected plagiarism. \
(3) Offering a solution by suggesting proper citation of paragraphs or requesting an extension for submission."


task_context = "Answer should convey an appropriate tone involving: \
(1) Empathy, expressing understanding towards Liu Hong's academic pressure and mental condition. \
(2) Seriousness, firmly discouraging any act of plagiarism in Liu Hong's essay. \
(3) Friendliness, offering suggestions or assistance regarding Liu Hong's essay issues."

task_context = "Hey Liu Hong, I just finished reading your essay, and I wanted to talk to you about it. First of all, I understand that you've been dealing with a lot of stress lately, and I'm here to support you. However, I noticed that the essay contains significant sections that are plagiarized from other sources. It's important to address this issue before you submit it. \
I know you might be feeling overwhelmed, but submitting a plagiarized paper can have serious consequences. It's crucial to maintain academic integrity. I strongly advise against submitting this essay as it is. \
I would be more than willing to help you improve the essay. Let's work together to rewrite the sections that are plagiarized and ensure that your ideas are properly cited. We can also work on enhancing the overall quality of the content. \
Remember, it's better to take the time to produce original work than to risk your academic standing. Let's discuss this further and come up with a plan to address the issue. You're not alone in this. Take care."

dir = "./task_tmp"
for file in os.listdir(dir):
    print(file)
    print(task_context)
    path = dir + "/" + file
    speechace.send_premium_task_request(path, task_type, task_context)
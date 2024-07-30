import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import ipdb
import numpy as np

'''
Relevant survey Qs:

'Does your institution host activities connected to astronomy-related instrumentation?'
 'What is the approximate expenditure of your institution in this area over the years 2019-2023?',
 'In your institution, what is the approximate distribution of instrumentation-focused personnel effort (FTE) given to (in percent):',
 'What would the ideal distribution of resources (funding and FTE) across the following areas look like for your institution (in percent)?',
 'Do you believe that overall funding received by your institute for astronomy instrumentation is:',
 'If changes to instrumentation funding could be made, how would you rank the following options in importance (1 being the most important):',
 'In the future, how does your institution expect its capacity in instrumentation-related activities to change?',
 'If you answered "Grow," which areas of growth have been identified (select all that apply)?',
 'If you answered “No change," what factors are inhibiting growth (select all that apply):',
 'If you answered "Reduce,” what factors are driving the reduction in capacity (select all that apply):',
 'What are the main benefits of instrumentation to your institution, the astronomy community, and society (select up to 5)?',
 'How would you rate the current level of collaboration between your research institution and industry partners? Please describe the institutional approach to collaboration and how extensively these collaborations are supported and encouraged at the institutional level',
 'In the past 5 years (2019-2023) have any higher-degree graduates at your institute completed an industry internship during their degree? (details are requested in the excel spreadsheet provided to institute contacts)',
 'What institutional strategies or initiatives do you believe could enhance industry engagement within the astronomy community?',
 'Does your institute have a clear policy and associated training on how to achieve industry engagement for translational research?',
 'Has your institute supported research initiatives involving industry, government, or international research organisations?',
 'Please provide short outline of size of project (years, approximate total cost,# persons) and short outline of nature of the project (e.g. new technology development, adapting commercial products, larger-scale build of existing astronomy-derived instrumentation etc).',
 'Did your institute utilize structured management processes or international standards (e.g. ISO9001) to implement the programs?',
 'Would your group benefit from further advice or training on industry engagement and translational research?',
 'Does your institute engage in research where significant intellectual property (IP) is or was generated by your organisation, or is expected to be generated?',
 "Did the contractual arrangement restrict either party's freedom to access, or otherwise further exploit, the IP?",
 'What were the reasons in your view for the success or failure in generation or transfer of IP?',
 'Was the partner able to commercially exploit the IP that resulted from the project or interaction?'
 'If yes, and if the partner was able to commercially exploit the IP, are you able to give a quantitative estimate of financial benefit or other impact?',
 "How developed do you consider your institute's skills to successfully exploit industry engagement opportunities and grants, commercial opportunities, industry capabilities and IP management?",
 'Do you believe that there is sufficient coordination and effort made within the Australian astronomy community to develop the flow of commercial products into, and IP out of, astronomy?',
 'Would your Institute be happy to be consulted further by NCA Decadal Plan WG3.3 Industry?',
 'Did your institution engage in the Australian Research Council Engagement and Impact Assessment (EIA) in 2018 or 2024 (now postponed)? If Yes do you have any example case studies highlighting fundamental research in astronomy with impact outcomes?',
 'Are you able to provide case summaries for applicable cases? Can we highlight these in the decadal plan?',
'''


def numerical_hbar(df_subset_pass, title_string, abcissa_string, norm_by=1, file_name='junk.png'):

    institutions = df_subset_pass.iloc[:, 0].tolist()
    responses = df_subset_pass.iloc[:, 1].tolist()
    # Converting responses to numeric values for plotting
    responses = [float(response) if float(response) > 0 else float(0) for response in responses]
    # if normalizing
    responses = np.divide(responses, norm_by)
    # Sorting by response size
    institutions, responses = zip(*sorted(zip(institutions, responses), key=lambda x: x[1]))
    # Plotting
    plt.figure(figsize=(10, len(institutions) * 0.5))
    plt.barh(institutions, responses, color='skyblue')
    plt.xlabel(abcissa_string)
    plt.title(title_string)
    plt.tight_layout()
    plt.savefig(file_name)
    plt.clf()
    print('Wrote',file_name)

    return


def yes_no_string(df_subset_pass, title_string, file_name='junk.png'):

    institutions = df_subset_pass.iloc[:, 0].tolist()
    responses = df_subset_pass.iloc[:, 1].tolist()
    # Plotting
    plt.clf()
    plt.figure(figsize=(5, len(institutions) * 0.5))
    for idx, (institution, response) in enumerate(zip(institutions, responses)):
        if response=='Yes':  # If the response is 'Yes'
            plt.plot(1, idx, marker='$Y$', markersize=10, color='g')  # Green Y for 'Yes'
        else:
            plt.plot(1, idx, marker='$N$', markersize=10, color='r')  # Red x for 'No' (or nan)
    plt.yticks(range(len(institutions)), institutions)
    plt.xticks([])  # Hide x-axis ticks
    plt.title(title_string)
    plt.tight_layout()
    plt.savefig(file_name)
    plt.clf()
    print('Wrote',file_name)

    return


def general_string(df_subset_pass, title_string, file_name='junk.png'):

    institutions = df_subset_pass.iloc[:, 0].tolist()
    responses = df_subset_pass.iloc[:, 1].tolist()
    # Plotting
    plt.clf()
    plt.figure(figsize=(5, len(institutions) * 0.5))
    for idx, (institution, response) in enumerate(zip(institutions, responses)):
        plt.text(0.1, idx-0.1, response, fontsize=12, color='k')
    plt.yticks(range(len(institutions)), institutions)
    plt.xticks([])  # Hide x-axis ticks
    plt.ylim([-0.5, len(institutions)])
    plt.title(title_string)
    plt.tight_layout()
    plt.savefig(file_name)
    plt.clf()
    print('Wrote',file_name)

    return


def main():

    stem = '/Users/bandari/Documents/git.repos/decadal/data/'

    df = pd.read_csv(stem + 'survey_data_cleaned.csv')

    df = df.drop(0)
    df_sorted = df.sort_values('For which Australian Astronomy institution/department are you reporting for?')

    # Does your institution host activities connected to astronomy-related instrumentation?
    df_subset = df[['For which Australian Astronomy institution/department are you reporting for?', 'Does your institution host activities connected to astronomy-related instrumentation?']]
    _ = yes_no_string(df_subset_pass=df_subset, 
                    title_string='Does your institution host activities connected to astronomy-related instrumentation?', 
                    file_name='junk0.png')

    # What is the approximate expenditure of your institution in this area over the years 2019-2023? (string)
    df_subset = df[['For which Australian Astronomy institution/department are you reporting for?','What is the approximate expenditure of your institution in this area over the years 2019-2023?']]
    _ = general_string(df_subset_pass=df_subset, 
                    title_string='What is the approximate expenditure of your institution in this area over the years 2019-2023?', 
                    file_name='junk1a.png')
    _ = numerical_hbar(df_subset_pass=df_subset, title_string = 'What is the approximate expenditure of your institution in this area over the years 2019-2023?', 
                    abcissa_string = '$M AUD', 
                    norm_by = 1e6,
                    file_name='junk1b.png')

    # In your institution, what is the approximate distribution of instrumentation-focused personnel effort (FTE) given to (in percent)
    df_subset = df[['For which Australian Astronomy institution/department are you reporting for?', 'How many full-time equivalence (FTE) employees work in Astronomy (including support staff) at your institution? (Please adjust for part-time work.)Include staff with unknown or non-binary gender in the total number. Detailed gender demographics will be collected by the individual survey']]
    _ = numerical_hbar(df_subset_pass=df_subset, title_string = 'How many full-time equivalence (FTE) employees work in Astronomy (including support staff) at your institution?', 
                    abcissa_string = 'Percent', 
                    norm_by = 1,
                    file_name='junk3.png')

    # What would the ideal distribution of resources (funding and FTE) across the following areas look like for your institution (in percent)?
    df_subset = df[['For which Australian Astronomy institution/department are you reporting for?', 'What would the ideal distribution of resources (funding and FTE) across the following areas look like for your institution (in percent)?']]
    _ = numerical_hbar(df_subset_pass=df_subset, title_string = 'What would the ideal distribution of resources (funding and FTE) across the following areas look like for your institution (in percent)?', 
                    abcissa_string = 'Percent', 
                    file_name='junk4.png')

    # 'Do you believe that overall funding received by your institute for astronomy instrumentation is
    df_subset = df[['For which Australian Astronomy institution/department are you reporting for?', 'Do you believe that overall funding received by your institute for astronomy instrumentation is:']]
    _ = general_string(df_subset_pass=df_subset, 
                    title_string='Do you believe that overall funding received by your institute for astronomy instrumentation is', 
                    file_name='junk5.png')

if __name__ == "__main__":
    main()
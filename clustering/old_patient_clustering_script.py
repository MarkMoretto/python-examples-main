
"""
Topic: Claims Grouping Analysis Exercise
Author: Mark Moretto
Date Created: 05/10/2018
"""


import gc
import os
import sys
import pyodbc
import random
import textwrap
import warnings
import numpy as np
import pandas as pd
from time import time
from time import sleep
from copy import deepcopy
from datetime import timedelta
from contextlib import suppress

from subprocess import call
from subprocess import check_output

from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score
from sklearn.exceptions import ConvergenceWarning
from sklearn.exceptions import DataConversionWarning

homeDir = r'C:\path\to\project\dir'
sys.path.append(homeDir)

from sklearn.cluster import KMeans
import BIC

def checkForBIC():
    modName = r'BIC'
    if modName not in sys.modules:
        try:
            from ..HelperScripts import BIC
        except:
            from .HelperScripts import BIC
        if modName not in sys.modules:
            try:
                from MyModules.Stats import BIC
            except ImportError:
                print('Warning! Module {} not imported!'.format(modName))


pd.options.mode.chained_assignment = None
pd.set_option('display.max_colwidth', -1)
pd.set_option('display.float_format', lambda x: '%.4f' % x)
gc.enable()

mainDir = r'C:\path\to\project\dir' # Folder for main project
tempOutPath = r'C:\path\to\temporary\dir' # Folder for holding temporary files.
eLog = r'C:\path\to\project\dir\errors.txt'

mySchema = r'MyTestDB'
tblName = 'DataClusters'

query1 = textwrap.dedent("""
""")


def getSqlData(input_query=query1):
    size = 0
    chunksize = 100000
    chunkList = []
    print('Reading data from SQL Server...')
    server = 'my_server'
    database = 'MyTestDB'
    conn = pyodbc.connect((r'DRIVER={SQL Server Native Client 11.0};SERVER={server=};DATABASE={database=};MARS_Connection=Yes;Trusted_Connection=yes'))
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute(input_query)
    conn.commit()
    query2 = "SELECT * FROM ##_temp_table"
    print('Current progress:')
    for chunk in pd.read_sql_query(query2, conn, chunksize=chunksize):
        size += chunksize
        print('\t~{:,} rows read'.format(size))
        chunkList.append(chunk)
    df = pd.concat(chunkList, axis=0)
    conn.close()
    return df


def timeConversion(float_time):
    if type(float_time) in [float, int]:
        float_time = np.float(float_time)
        timeMain = str(timedelta(seconds=float_time))
        t_h, t_m, t_s = timeMain.split('.')[0].split(':')
        if t_h == '0':
            print('\nTime elapsed: {} minutes, {} seconds'.format(int(t_m), int(t_s)))
        elif t_m == '0':
            print('\nTime elapsed: {} seconds'.format(int(t_s)))
        elif t_s == '0':
            print('\nError! Issue with data import!')
        else:
            print('\nTime elapsed: {} hours, {} minutes, {} seconds'.format(int(t_h), int(t_m), int(t_s)))
    else:
        print('\nError! Time needs to be in float format!')


def trincateClusterTable(table_path):
    truncateTblSql = r'TRUNCATE TABLE {}'.format(table_path)
    server = 'my_server'
    database = 'MyTestDB'
    conn = pyodbc.connect((r'DRIVER={SQL Server Native Client 11.0};SERVER={server=};DATABASE={database=};MARS_Connection=Yes;Trusted_Connection=yes'))
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute(truncateTblSql)
    conn.commit()
    conn.close()


def importData():
    t_start = time()
    data = getSqlData()
    t_end = time() - t_start
    timeConversion(t_end)
    return data


def cleanData():

    from sklearn.preprocessing import Imputer
    impute = Imputer(missing_values='NaN', strategy='median', axis=0)

    mainDF = importData()
    # dataDF = getSqlData()
    listDict = {k:v for k, v in enumerate(mainDF)}
    toExclude = [0]
    df = mainDF[[listDict[k] for k in listDict if k not in toExclude]]

    X_array = impute.fit_transform(df)
    return X_array, mainDF

def runGMM(X):

    GMM_cov_types = [
        'spherical', 
        'full'
        ]
    scoreMetrics = [
        'braycurtis',
        'canberra',
        'chebyshev',
        'correlation',
        'cosine',
        'euclidean',
        'hamming',
        'l1',
        'l2',
        'kulsinski',
        'manhattan',
        'minkowski',
        'rogerstanimoto',
        'sqeuclidean'
        ]
    metDict = {k + 1: v for k, v in enumerate(scoreMetrics)}
    randMetrics = random.sample(range((len(metDict.keys())) + 1), 5)
    # print('\nThe randomly selected evaluation metrics are: \n\t\'{}\''.format('\', \n\t\''.join([metDict[k] for k in metDict.keys() if k in randMetrics])))

    eval_list = []
    lowBic = np.infty
    lowScore = np.infty

    dd = dict()
    ed = dict()

    def warnList():
        warnings.warn("ConversionWarning", DataConversionWarning)
        warnings.warn("ConvergeWarning", ConvergenceWarning)

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        warnList()
        np.seterr(divide='ignore', invalid='ignore')

        for item in GMM_cov_types:
            print('\nCurrently evaluating with covariance \'{}\''.format(item))
            dd[item] = dict()
            ed[item] = dict()
            t_start_o = time()
            gmm = GaussianMixture(n_components=10, covariance_type=item, max_iter=100)
            gmm.fit(X)
            # tempLabel = gmm.predict(X)
            # gc.collect(2)
            # for k in metDict.keys():
            #     if k in randMetrics:
            #         dd[item][metDict[k]] = dict()
            #         silScore = silhouette_score(X, labels=tempLabel, metric = str(metDict[k]), sample_size = 1000)
            #         print("\tThe avg. silhouette score for metric \'{}\' is: {:0.3f}".format(metDict[k], silScore))
            #         dd[item][metDict[k]] = silScore
            vBic = gmm.bic(X)
            vAIC = gmm.aic(X)
            print('The BIC for \'{}\' is: {:<35.6f}'.format(item, vBic))
            eval_list.append(vBic)
            ed[item] = vBic
            dd[item]['bic'] = vBic
            dd[item]['aic'] = vAIC
            t_end_o = time() - t_start_o
            timeConversion(t_end_o)
            if eval_list[-1] < lowBic:
                lowBic = eval_list[-1]
                bestModel = gmm
                gc.collect(2)

    # labelsGMM = bestModel.predict(X)
    # labels = labelsGMM + 1
    return bestModel, dd, ed


def runKMeans(X):

    _bic = BIC.compute_bic

    eval_list = []
    lowBIC = np.infty

    thresholds = [0.0001, 0.0002, 0.0005]
    dd = dict()
    ed = dict()

    for thresh in thresholds:
        dd[thresh] = dict()
        ed[thresh] = dict()
        t_start = time()
        print('\nNow running K-Means with threshold \'{}\''.format(thresh))
        kmm = KMeans(n_clusters=10, max_iter=100, tol=thresh)
        kmm.fit(X)
        vBIC = _bic(kmm, X)
        print('\tThe BIC for threshold \'{}\' is: {:<20.6f}'.format(thresh, vBIC))
        eval_list.append(vBIC)
        ed[thresh] = vBIC
        dd[thresh]['bic'] = dict()
        dd[thresh]['bic'] = vBIC
        t_end = time() - t_start
        timeConversion(t_end)
        if eval_list[-1] < lowBIC:
            lowBIC = eval_list[-1]
            bestModel = kmm

    return bestModel, dd, ed


def modelCompare():

    X, df_orig = cleanData()
    ### Capture the model and relvant dictionary from each run
    bestGMM, _, eDictGMM = runGMM(X)
    bestKMM, _, eDictKMM = runKMeans(X)

    ### Get minimum BIC values from each model
    Key_GMM = min(eDictGMM, key=eDictGMM.get)
    Key_KMM = min(eDictKMM, key=eDictKMM.get)

    ### Determine the lowest BIC and make that the selected model
    if eDictGMM[Key_GMM] < eDictKMM[Key_KMM]:
        bestModel = bestGMM
        modelName = 'Gaussian Mixed'
    else:
        bestModel = bestKMM
        modelName = 'K-Means'

    ### Run the model to get the new labels and add 1 to bring them
    ### into a range of 1 - 10
    vLabels = bestModel.predict(X)
    labelOut = vLabels + 1

    ### Return the reformatted labels and model name
    return labelOut, modelName, df_orig


def reformatAndLoad():

    labels, topModelName, main_df = modelCompare()

    main_df['Groups'] = labels.ravel()[:]
    df_out = main_df[['DurableKey','Groups']]
    df_out['DurableKey'] = df_out['DurableKey'].apply(lambda x: str(x).strip())

    return df_out, topModelName

def loadToSSMS(df, schema=mySchema, tableName=tblName, path_out=tempOutPath):

    server = r'ClaritySNAP'
    database = r'EDWUsersDB'

    shortTable = '{}.{}'.format(schema, tableName)
    tableNameFull = '{}.{}.{}'.format(database, schema, tableName)
    tableNameBracket = '[{}].[{}].[{}]'.format(database, schema, tableName)

    cFormatFile = r'C:\Users\mmorett1\Desktop\formatFiles\{}_Format.fmt'.format(tableName)
    call('bcp {} format nul -T -c -t` -S {} -f "{}"'.format(tableNameFull, server, cFormatFile))

    tempFileName = '{}_temp.txt'.format(tableName)
    outPathFull =  os.path.join(path_out, tempFileName)
    df.to_csv(outPathFull, sep='`', index=False)

    print('Clearing out old data...')
    trincateClusterTable(tableNameBracket)

    print('Loading new data...')
    g = call('bcp {} in "{}" -S {} -T -t` -d {} -f "{}" -e "{}" -F 2 -r "0x0a"'.format(shortTable, outPathFull, server, database, cFormatFile, eLog))
    if g != 0:
        raise BaseException("Failed to load data!")
    

    print('\nData load complete!')
    return outPathFull

def main():
    checkForBIC()
    # X, df = cleanData()
    # labl, modName, df = modelCompare()
    df, modName = reformatAndLoad()
    outPath = loadToSSMS(df)
    print('{} refresh complete!'.format(tblName))
    print('Today\'s best model was: \'{}\''.format(modName))
    with suppress(FileNotFoundError):
        os.remove(outPath)
    input('Press any key to exit.')
    sleep(1)
    print('Goodbye!')
    sleep(1)
    sys.exit(0)


if __name__ == '__main__':
    main()

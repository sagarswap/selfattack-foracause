import pandas as pd
import numpy as np

content=pd.read_csv('./data/cyberml_-_cyberml.csv')
for (columnName, columnData) in content.iteritems():
    content[columnName]=content[columnName].apply(hash)
# content.drop('_source.timestamp', axis=1)
# content=content.apply(hash)
# print(content)
#print(content.cov())
lessContent=content[['_source.rule.firedtimes', '_source.rule.id', '_source.id', '_source.syscheck.size_after', '_source.syscheck.inode_after', '_source.syscheck.size_before', '_source.syscheck.inode_before', 'malicious']]
print(content)
content.to_csv('./data/processedData.csv', index=False)
lessContent.to_csv('./data/processedLessData.csv', index=False)

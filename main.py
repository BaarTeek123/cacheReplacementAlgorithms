from random import randint
import generator
import replacePage

if __name__ == '__main__':
    amountOfFrames = 7
    amount=1000
    filePath='TESTY\\Strony\\n=15 ramek 5 7 M=10 SD=5'
    pages= replacePage.importList(filePath+'\\Strony.txt')
    fifo, faultsFIFO = replacePage.fifo(pages, amountOfFrames)
    lru, faultsLRU = replacePage.lru(pages, amountOfFrames)
    mfu, faultsMFU = replacePage.mfu(pages, amountOfFrames)
    lfu, faultsLFU = replacePage.lfu(pages, amountOfFrames)
    print('FIFO', amountOfFrames)
    # replacePage.printFrames(fifo)
    print('BŁĘDY', faultsFIFO)
    print('LRU', amountOfFrames)
    # replacePage.printFrames(lru)
    print('BŁĘDY', faultsLRU)
    print('LFU', amountOfFrames)
    # replacePage.printFrames(lfu)
    print('BŁĘDY', faultsLFU)
    print('MFU', amountOfFrames)
    # replacePage.printFrames(mfu)
    print('BŁĘDY', faultsMFU)

    # # znajdowanie anomalii Beladiego
    # firstAmountOfFrames = 5
    # secondAmountOfFrames = 4
    # start = 1
    # stop = 6
    # amount = 20
    # pagesA, faultsA, pagesB, faultsB = replacePage.BeladyAnomaly(firstAmountOfFrames,secondAmountOfFrames,start,stop,amount)
    # replacePage.printFrames(pagesA)
    # print('Błedy A:', faultsA)
    # replacePage.printFrames(pagesB)
    # print('Błedy B:', faultsB)

    amountOfFrames=5
    fifo, faultsFIFO = replacePage.fifo(pages, amountOfFrames)
    lru, faultsLRU = replacePage.lru(pages, amountOfFrames)
    mfu, faultsMFU = replacePage.mfu(pages, amountOfFrames)
    lfu, faultsLFU = replacePage.lfu(pages, amountOfFrames)
    print('FIFO', amountOfFrames)
    # replacePage.printFrames(fifo)
    print('BŁĘDY', faultsFIFO)
    print('LRU', amountOfFrames)
    # replacePage.printFrames(lru)
    print('BŁĘDY', faultsLRU)
    print('LFU', amountOfFrames)
    # replacePage.printFrames(lfu)
    print('BŁĘDY', faultsLFU)
    print('MFU', amountOfFrames)
    # replacePage.printFrames(mfu)
    print('BŁĘDY', faultsMFU)

    #wysłanie do pliku
    # replacePage.importData(lfu,amountOfFrames,faultsLFU,'LFU3','C:\\Users\\user\\PycharmProjects\\projektSO\\TESTY\\Strony\\LFU1.xlsx')
    # replacePage.importData(mfu,amountOfFrames,faultsMFU,'MFU3','C:\\Users\\user\\PycharmProjects\\projektSO\\TESTY\\Strony\\MFU1.xlsx')
    # replacePage.importData(fifo,amountOfFrames,faultsFIFO,'FIFO3','C:\\Users\\user\\PycharmProjects\\projektSO\\TESTY\\Strony\\FIFO1.xlsx')
    # replacePage.importData(lru,amountOfFrames,faultsLRU,'LRU3','C:\\Users\\user\\PycharmProjects\\projektSO\\TESTY\\Strony\\LRU1.xlsx')




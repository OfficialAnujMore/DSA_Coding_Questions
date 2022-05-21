from platform import java_ver


class Request :
    def __init__(self, arrivalTime,  processTime) :
        self.arrivalTime = arrivalTime
        self.processTime = processTime
    arrivalTime = 0
    processTime = 0
class Response :
    def __init__(self, dropped,  startTime) :
        self.dropped = dropped
        self.startTime = startTime
    dropped = False
    startTime = 0
class Buffer :
    def __init__(self, size) :
        self.size = size
        self.queue =  java_ver.util.LinkedList()
        self.finishTime = 0
    def  process(self, request) :
        while (self.queue.size() > 0 and self.queue.peekFirst() <= request.arrivalTime) :
            self.queue.removeFirst()
        if (self.queue.size() >= self.size) :
            # buffer full
            return Response(True, -1)
        if (self.queue.size() <= 0) :
            # empty buffer
            self.finishTime += request.processTime
            self.queue.add(self.finishTime)
            return Response(False, request.arrivalTime)
        self.finishTime = self.queue.peekLast()
        r = Response(False, self.finishTime)
        self.finishTime += request.processTime
        self.queue.addLast(self.finishTime)
        return r
    size = 0
    queue = None
    finishTime = 0
class ProcessPackage :
    @staticmethod
    def  readQueries( scanner) :
        requestsCount = input()
        requests =  []
        i = 0
        while (i < requestsCount) :
            arrivalTime = input()
            processTime = input()
            requests.append(Request(arrivalTime, processTime))
            i += 1
        return requests
    @staticmethod
    def  processRequests( requests,  buffer) :
        responses =  []
        i = 0
        while (i < len(requests)) :
            responses.append(buffer.process(requests[i]))
            i += 1
        return responses
    @staticmethod
    def printResponses( responses) :
        i = 0
        while (i < len(responses)) :
            response = responses[i]
            if (response.dropped) :
                print(-1)
            else :
                print(response.startTime)
            i += 1
    @staticmethod
    def main( args) :
        scanner =  "Python-inputs"
        bufferSize = input()
        buffer = Buffer(bufferSize)
        requests = ProcessPackage.readQueries(scanner)
        responses = ProcessPackage.processRequests(requests, buffer)
        ProcessPackage.printResponses(responses)
    

if __name__=="__main__":
    ProcessPackage.main([])
class Solution {
public:

    bool DFS(int source, int destination, vector<vector<int>>& adj, vector<int>& visited) {

        if (source == destination) {
            return true;
        }

        visited[source] = 1;

        for (int i : adj[source]) {

            if (visited[i] == 0) {

                if (DFS(i, destination, adj, visited)) {
                    return true;
                }
            }
        }

        return false;
    }


    bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {

        vector<vector<int>> adj(n);

        for (int i = 0; i < edges.size(); i++) {

            int x = edges[i][0];
            int y = edges[i][1];

            adj[x].push_back(y);
            adj[y].push_back(x);
        }

        vector<int> visited(n, 0);

        return DFS(source, destination, adj, visited);
    }
};





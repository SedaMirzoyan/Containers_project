#include <iostream>
#include <vector>
#include <list>
#include <string>

template <typename K, typename V>

class Hash_Table 
{
private:
    std::vector<std::list<std::pair<K, V>>> m_table;
    int m_size;

public:
    Hash_Table(int size = 10)
    {
        m_size = 0;
        m_table.resize(size);
    }


    int hash_func(const K& key) const 
    {
        return std::hash<K>{}(key) % m_table.size();
    }

    void insert(const K& key, const V& value) 
    {
        int index = hash_func(key);
        auto bucket = m_table[index];

        for (auto& pair : bucket) 
        {
            if (pair.first == key) 
            {
                pair.second = value;
                return;
            }
        }

        bucket.emplace_back(key, value);
        m_size++;
    }


    bool get(const K& key, V& value) const 
    {
        int index = hash_func(key);
        const auto& bucket = m_table[index];

        for (const auto& pair : bucket) 
        {
            if (pair.first == key) 
            {
                value = pair.second;
                return true;
            }
        }
        return false;
    }

    void remove(const K& key) 
    {
        int index = hash_func(key);
        auto& bucket = m_table[index];

        auto it = std::find_if(bucket.begin(), bucket.end(), [key](const auto& pair) 
            {
                return pair.first == key;
            });

        if (it != bucket.end()) 
        {
            bucket.erase(it);
            m_size--;
        }
    }

};

int main()
{
    Hash_Table<std::string, int> ht;

    ht.insert("blue", 1);
    ht.insert("yellow", 2);
    ht.insert("green", 3);
    int val;
    ht.get("blue", val);
    ht.remove("green");

    return 0;
}
